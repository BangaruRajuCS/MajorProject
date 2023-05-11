from typing import Dict
from src.Model.Post import Post
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class ConversationTree:

    def __init__(self, initiatedAuthorId: int, discussionId: int, discussionTitle: str, posts: Dict[str, Post]):
        self.initiatedAuthorId = initiatedAuthorId
        self.discussionId = discussionId
        self.discussionTitle = discussionTitle
        self.tree = {}
        self.originalPost = str(initiatedAuthorId) + "_" + str(discussionTitle)
        self.tree[self.originalPost] = []
        self.posts = posts
        self.buildConversationTree()

    def buildConversationTree(self):
        for post in self.posts.values():
            if post.discussionId == self.discussionId:
                if np.isnan(post.parentPostId):
                    self.tree[self.originalPost].append(str(post.postId))
                elif str(post.parentPostId) not in self.tree.keys():
                    self.tree[str(post.parentPostId)] = []
                    self.tree[str(post.parentPostId)].append(str(post.postId))
                else:
                    self.tree[str(post.parentPostId)].append(str(post.postId))

    def showConversationTree(self):
        diGraph = nx.DiGraph()
        for node in self.tree.keys():
            diGraph.add_node(str(node))
        for node in self.tree.keys():
            for reply in self.tree[node]:
                diGraph.add_edge(str(reply), str(node))
        nx.draw(diGraph,with_labels=True)
        plt.show()


    def getConversationTree(self):
        return self.tree
