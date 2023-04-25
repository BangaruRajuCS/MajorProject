from src.Service.ConversationTree import ConversationTree
import networkx as nx
from typing import List
from src.Model.Quote import Quote
import matplotlib.pyplot as plt


class InteractionNetwork:

    def __int__(self, conversationTree: ConversationTree, quotes: List[Quote]):
        self.conversationTree = conversationTree
        self.graph = nx.Graph()
        self.quotes = quotes

    def __init__(self,conversationTree:ConversationTree,quotes):
        self.conversationTree = conversationTree
        self.graph = nx.Graph()
        self.quotes = quotes
        self.buildInteractionNetwork()

    def buildInteractionNetwork(self):
        for post in self.conversationTree.posts.values():
            self.graph.add_node(str(post.authorId))
        self.graph.add_node(str(self.conversationTree.originalPost))
        for node in self.conversationTree.tree.keys():
            u = self.conversationTree.originalPost
            if node != self.conversationTree.originalPost:
                u = str(self.conversationTree.posts[str(node)].authorId)
            for anotherPost in self.conversationTree.tree[str(node)]:
                v=str(self.conversationTree.posts[str(anotherPost)].authorId)
                args = self.graph.get_edge_data(u, v, -1)
                if args != -1:
                    self.graph.remove_edge(u, v)
                    weight = args['weight'] + 1
                    self.graph.add_edge(u, v, weight=weight)
                else:
                    self.graph.add_edge(u, v, weight=1)

                print(self.graph.get_edge_data(u,v))


    def showInteractionNetwork(self):
        nx.draw(self.graph,with_labels=True,width=[self.graph[u][v]['weight'] for u,v in self.graph.edges()])
        plt.show()
