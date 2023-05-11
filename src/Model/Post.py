import pandas
import numpy as np
class Post:
	def __init__(self,discussionId,authorId,postId,parentPostId,responseType=""):
		self.discussionId = discussionId
		self.authorId = authorId
		self.postId=postId
		self.parentPostId=parentPostId
		if not np.isnan(self.parentPostId):
			self.parentPostId=int(parentPostId)
		self.responseType=responseType
