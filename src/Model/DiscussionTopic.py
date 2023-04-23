import pandas
# import glob
class DiscussionTopic:
	def __init__(self):
		#directory_path = 'Users\\vaishu\\Desktop\\Project\\MPphase2\\input'
		#Retriving disucssion stance datasheet from createdebate execel 
		discussionTopicSheet = pandas.read_excel('createdebate_released_no_parse.xlsx', sheet_name='discussion_topic')
        # Retiving particular coloumn form the sheet
		self.__discussionId = discussionTopicSheet['discussion_id']
		self.__topicId=discussionTopicSheet['topic_id']
	#get and set function for discussion id variable
	def get_discussinId(self):
		return self.__discussionId
	def set_discussionId(self,value):
		self.__discussionId=value
	#get and set function for title variable
	def get_topicId(self):
		return self.__topicId
	def set_topicId(self,value):
		self.__topicId=value
#create an object to the Discussion Class
obj=DiscussionTopic()
#use the getter methods to acccess the private variables
print(obj.get_discussinId())
print('...........................................................')
print(obj.get_topicId())
