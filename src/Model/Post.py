import pandas
class Post:
	def __init__(self,discussionId,authorId,parentPostId,responseType):
		self.discussionId = discussionId
		self.authorId = authorId
		self.parentPostId=parentPostId
		self.responseType=responseType
