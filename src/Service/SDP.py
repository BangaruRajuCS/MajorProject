import networkx as nx
import cvxpy as cvx
import numpy as np


class User:
    def __init__(self, userId, stance):
        self.userId = userId
        self.stance = stance
    def __str__(self):
        temp="{userId : "+str(self.userId)+"\n"
        temp=temp+"stance  : "+str(self.stance)+"}"
        return temp


class Result:
    def __init__(self, cost, cut):
        self.cost = cost
        self.cut = cut

    def __str__(self):
        print("{Cost : ",self.cost)
        print("Cut   : ",end=" ")
        for i in range(len(self.cut)):
            print(self.cut[i])
        return ""


class SDP:

    def __init__(self, graph: nx.Graph):
        self.graph = graph
        self.results = []

    def runSDP(self):
        n = self.graph.number_of_nodes()
        L = nx.laplacian_matrix(self.graph, nodelist=sorted(self.graph.nodes))
        # SDP solution
        X = cvx.Variable((n, n), PSD=True)
        obj = 0.25 * cvx.trace(L.toarray() * X)
        constr = [cvx.diag(X) == 1]
        problem = cvx.Problem(cvx.Maximize(obj), constraints=constr)
        problem.solve(solver=cvx.SCS)
        activeUsers = sorted(list(self.graph.nodes))

        # GW algorithm
        # u, s, v = np.linalg.svd(X.value)
        # U = u * np.sqrt(s)
        matrix = self.getNearestPSD(X.value)
        U = np.linalg.cholesky(matrix)
        k = U.T
        num_trials = 30
        for i in range(num_trials):
            r = np.random.randn(n)
            r = r / np.linalg.norm(r)
            cut = np.sign(r @ U.T)
            cost = self.getCutCost(cut, L)
            cutUsers = self.getCutUsers(cut, activeUsers)
            result = Result(cost, cutUsers)
            self.results.append(result)
        self.results.sort(key=lambda result: result.cost)

    def getCutCost(self, x, L):
        return 0.25 * x @ L @ x

    def getNearestPSD(self, matrix):
        if self.isPSD(matrix):
            return matrix
        spacing = np.spacing(np.linalg.norm(matrix))
        identity = np.identity(len(matrix))
        k = 1
        while not self.isPSD(matrix):
            min_eig = np.min(np.real(np.linalg.eigvals(matrix)))
            matrix += identity * (- min_eig * (k ** 2) + spacing)
            k += 1
        return matrix

    def isPSD(self, matrix):
        try:
            _ = np.linalg.cholesky(matrix)
            return True
        except np.linalg.LinAlgError:
            return False

    def getCutUsers(self, cut, activeUsers):
        users = []
        for i in range(len(activeUsers)):
            user = User(activeUsers[i], cut[i])
            users.append(user)
        return users

    def getBestCut(self) -> Result:
        return self.results[-1]
