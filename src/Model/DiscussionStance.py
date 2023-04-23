import pandas
# import glob
class DiscussionStance:
	def __init__(self):
		#directory_path = 'Users\\vaishu\\Desktop\\Project\\MPphase2\\input'
		#Retriving disucssion Stance datasheet from createdebate execel 
		discussionStanceSheet = pandas.read_excel('createdebate_released_no_parse.xlsx', sheet_name='discussion_stance')
        # Retiving particular coloumn from the sheet
		self.__discussionId = discussionStanceSheet['discussion_id']
		self.__discussionStance=discussionStanceSheet['discussion_stance']
		self.__topicId=discussionStanceSheet['topic_id']
		self.__topicStanceId=discussionStanceSheet['topic_stance_id']
	#get and set function for discussion id variable
	def get_discussinId(self):
		return self.__discussionId
	def set_discussionId(self,value):
		self.__discussionId=value
	#get and set function for discussionStance variable
	def get_discussionStance(self):
		return self.__discussionStance
	def set_discussionStance(self,value):
		self.__discussionStance=value
	#get and set function for topic id variable
	def get_topicId(self):
		return self.__topicId
	def set_topicId(self,value):
		self.__topicId=value
	#get and set function for topic stance id variable
	def get_topicStanceId(self):
		return self.__topicStanceId
	def set_topicStanceId(self,value):
		self.__topicStanceId=value
#create an object to the Discussion Class
obj=DiscussionStance()
#use the getter methods to acccess the private variables
print(obj.get_discussinId())
print('...........................................................')
print(obj.get_discussionStance())
print('...........................................................')
print(obj.get_topicId())
print('...........................................................')
print(obj.get_topicStanceId())

