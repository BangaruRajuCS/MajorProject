import pandas
# import glob
class Discussion:
	def __init__(self):
		#directory_path = 'C:\\Users\\vaishu\\Desktop\\Project\\MPphase2\\input'
		#Retriving disucssion datasheet from createdebate execel 
		DiscussionSheet = pandas.read_excel('createdebate_released_no_parse.xlsx', sheet_name='discussion')
        # Retiving particular coloumn form the sheet
		self.__discussionId = DiscussionSheet['discussion_id']
		self.__title=DiscussionSheet['title']
		self.__initiatingAuthorId=DiscussionSheet['initiating_author_id']
	#get and set function for discussion id variable
	def get_discussinId(self):
		return self.__discussionId
	def set_discussionId(self,value):
		self.__discussionId=value
	#get and set function for title variable
	def get_title(self):
		return self.__title
	def set_title(self,value):
		self.__title=value
	#get and set function for initiating author id variable
	def get_initiatingAuthorId(self):
		return self.__initiatingAuthorId
	def set_initiatingAuthorId(self,value):
		self.__initiatingAuthorId=value
#create an object to the Discussion Class
obj=Discussion()
#use the getter methods to acccess the private variables
print(obj.get_discussinId())
print('...........................................................')
print(obj.get_title())
print('...........................................................')
print(obj.get_initiatingAuthorId())
