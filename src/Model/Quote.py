import pandas
# import glob
class Quote:
	def __init__(self,filePath):
		#directory_path = 'Users\\vaishu\\Desktop\\Project\\MPphase2\\input'
		#Retriving disucssion datasheet from createdebate execel 
		quoteSheet = pandas.read_excel(filePath, sheet_name='quote')
        # Retiving particular coloumn form the sheet
		self.__discussionId = quoteSheet['discussion_id']
		self.__postId=quoteSheet['post_id']
		self.__sourcePostId=quoteSheet['source_post_id']
	#get and set function for discussion id variable
	def get_discussionId(self):
		return self.__discussionId
	def set_discussionId(self,value):
		self.__discussionId=value
	#get and set function for title variable
	def get_postId(self):
		return self.__postId
	def set_postId(self,value):
		self.__postId=value
	#get and set function for initiating author id variable
	def get_sourcePostId(self):
		return self.__sourcePostId
	def set_sourcePostId(self,value):
		self.__sourcePostId=value
#create an object to the Discussion Class
obj=Quote()
#use the getter methods to acccess the private variables
print(obj.get_discussionId())
print('...........................................................')
print(obj.get_postId())
print('...........................................................')
print(obj.get_sourcePostId())
