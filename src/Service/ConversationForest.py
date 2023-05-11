from src.Service.LoadInput import LoadInput
from src.Service.ConversationTree import ConversationTree
from src.Model.Discussion import Discussion
from typing import Dict


class ConversationForest:

    def __init__(self, loadInputObject: LoadInput):
        self.loadInputObject = loadInputObject
        self.conversationTrees: Dict[str, ConversationTree] = {}

    def buildConversationTrees(self):
        discussionRecords = self.loadInputObject.discussionRecords
        for key, value in discussionRecords.items():
            self.conversationTrees[key] = self.buildConversationTree(value)

    def buildConversationTree(self, discussion: Discussion):
        initiatedAuthorId = discussion.initiatingAuthorId
        discussionId = discussion.discussionId
        discussionTitle = discussion.title
        posts = {}
        for post in self.loadInputObject.postRecords.values():
            if post.discussionId == discussionId:
                posts[str(post.postId)] = post
        conversationTree = ConversationTree(initiatedAuthorId, discussionId, discussionTitle, posts)
        return conversationTree

    def getAllConversationTrees(self):
        return self.conversationTrees
