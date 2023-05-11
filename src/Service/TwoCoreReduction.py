import networkx as nx


class TwoCoreReduction:

    def __init__(self, graph: nx.Graph):
        self.graph = graph

    def run2CoreReduction(self) -> nx.Graph:
        self.cleanGraph()
        newGraph = nx.k_core(self.graph, k=2)
        return newGraph

    def cleanGraph(self):
        self.graph.remove_edges_from(nx.selfloop_edges(self.graph))
