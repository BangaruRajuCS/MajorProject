import networkx as nx


class TwoCoreReduction:

    def __init__(self, graph: nx.Graph):
        self.graph = graph

    def run2CoreReduction(self):
        self.cleanGraph()
        self.graph = nx.k_core(self.graph, k=2)
        return self.graph

    def cleanGraph(self):
        self.graph.remove_edges_from(nx.selfloop_edges(self.graph))
