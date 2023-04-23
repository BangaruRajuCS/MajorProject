import pandas
# import glob
class Post:
	def __init__(self):
		#directory_path = 'Users\\vaishu\\Desktop\\Project\\MPphase2\\input'
		#Retriving post datasheet from createdebate execel 
		postSheet = pandas.read_excel('createdebate_released_no_parse.xlsx', sheet_name='post')
        # Retiving particular coloumn form the sheet
		self.__discussionId = postSheet['discussion_id']
		self.__postId=postSheet['post_id']
		self.__authorId = postSheet['author_id']
		self.__parentPostId=postSheet['parent_post_id']
		self.__responseType=postSheet['response_type']
	#get and set function for discussion id variable
	def get_discussionId(self):
		return self.__discussionId
	def set_discussionId(self,value):
		self.__discussionId=value
	#get and set functions for postId variable
	def get_postId(self):
		return self.__postId
	def set_postId(self,value):
		self.__postId=value
	#get and set functions for authorId variable
	def get_authorId(self):
		return self.__authorId
	def set_authorId(self,value):
		self.__postId=value
	#get and set functions for parentPostId variable
	def get_parentPostId(self):
		return self.__parentPostId
	def set_parentPostId(self,value):
		self.__parentPostId=value
	#get and set functions for responseType variable
	def get_responseType(self):
		return self.__responseType
	def set_responseType(self,value):
		self.__responseType=value
#create an object to the Discussion Class
obj=Post()
#use the getter methods to acccess the private variables
print(obj.get_discussionId())
print('...........................................................')
print(obj.get_postId())
print('...........................................................')
print(obj.get_authorId())
print('...........................................................')
print(obj.get_parentPostId())
print('...........................................................')
print(obj.get_responseType())
