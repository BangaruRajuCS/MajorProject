from typing import List
from ..Model.Post import Post

class ConversationTree:

    def __init__(self, initiatedAuthorId:int, discussionId:int,discussionTitle:str, posts:List[Post]):
        self.initiatedAuthorId = initiatedAuthorId
        self.discussionId=discussionId
        self.discussionTitle = discussionTitle
        self.tree = {}
        self.posts = posts


    def buildConversationTree(self):
        '''
        to work
        :return:
        '''
        for post in self.posts:





    def showConversationTree(self):
        '''
        to do work
        :return:
        '''

    def getConversationTree(self):
        '''
        to do work
        :param topic:
        :return:
        '''
