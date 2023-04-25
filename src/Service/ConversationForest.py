from LoadInput import LoadInput
from ConversationTree import ConversationTree
from ..Model.Discussion import Discussion


class ConversationForest:

    def __int__(self, loadInputObject: LoadInput):
        self.conversationTrees = {}
        self.loadInputObject = loadInputObject

    def buildConversationTrees(self):
        discussionRecords = self.loadInputObject.discussionRecords
        for key, value in discussionRecords.items():
            self.conversationTrees[key] = self.buildConversationTree(value)

    def buildConversationTree(self, discussion: Discussion):
        initiatedAuthorId = discussion.initiatingAuthorId
        discussionId = discussion.discussionId
        discussionTitle = discussion.title
        posts = {}
        for post in self.loadInputObject.postRecords:
            if post.discussionId == discussionId:
                posts[post.postId] = post

        conversationTree = ConversationTree(initiatedAuthorId, discussionId, discussionTitle, posts)
        return conversationTree

    def getAllConversationTrees(self):
        return self.conversationTrees



