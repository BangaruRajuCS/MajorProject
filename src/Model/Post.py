import pandas
class Post:
	def __init__(self,discussionId,authorId,postId,parentPostId,responseType):
		self.discussionId = discussionId
		self.authorId = authorId
		self.postId=postId
		self.parentPostId=parentPostId
		self.responseType=responseType
