import networkx as nx
import cvxpy as cvx
import numpy as np


class SDP:

    def __init__(self, graph: nx.Graph):
        self.graph = graph

    def runSDP(self):
        n = self.graph.number_of_nodes()
        L = nx.laplacian_matrix(self.graph, nodelist=sorted(self.graph.nodes))
        # SDP solution
        X = cvx.Variable((n, n), PSD=True)
        obj = 0.25 * cvx.trace(L.toarray() * X)
        constr = [cvx.diag(X) == 1]
        problem = cvx.Problem(cvx.Maximize(obj), constraints=constr)
        problem.solve(solver=cvx.SCS)

        # GW algorithm
        # u, s, v = np.linalg.svd(X.value)
        # U = u * np.sqrt(s)
        matrix = self.nearest_psd(X.value)
        U = np.linalg.cholesky(matrix)
        num_trials = 30
        gw_results = np.zeros(num_trials)
        for i in range(num_trials):
            r = np.random.randn(n)
            print("r")
            print(r)
            r = r / np.linalg.norm(r)
            cut = np.sign(r @ U.T)
            print("Cut")
            print(cut)
            gw_results[i] = self.cut_cost(cut, L)

        print(gw_results)

    def cut_cost(self, x, L):
        return 0.25 * x @ L @ x

    def nearest_psd(self, matrix):
        if self.is_psd(matrix):
            return matrix
        spacing = np.spacing(np.linalg.norm(matrix))
        identity = np.identity(len(matrix))
        k = 1
        while not self.is_psd(matrix):
            min_eig = np.min(np.real(np.linalg.eigvals(matrix)))
            matrix += identity * (- min_eig * (k ** 2) + spacing)
            k += 1
        return matrix

    def is_psd(self, matrix):
        try:
            _ = np.linalg.cholesky(matrix)
            return True
        except np.linalg.LinAlgError:
            return False
