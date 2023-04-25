import pandas
import sys
sys.path.insert(1, 'C:/Users/vaishu/Desktop/Project/MPphase2/src/Model')
from Discussion import Discussion
from Author import Author
from DiscussionStance import DiscussionStance
from DiscussionTopic import DiscussionTopic
from Post import Post
from Quote import Quote
from Topic import Topic
from TopicStance import TopicStance
# import Author.py
#or every row in AuthorSheet 
'''
    Format:
        authorRecords ={ key=authorId ,value=AuthorClass }
        discussionRecords={key=discussionId value=DiscussionClass}
        discussionStanceRecords={key =discussion_id+discussion_stance_id value=DiscussionStanceClass}
        discussionTopicRecords={key=discussionId+topicId value=DiscussionTopicClass}
        postRecords={key=postId value=PostClass}
        quoteRecords={key=postId+SourcePostId value=QuoteClass}
        topicRecords={key=topicId value=TopicClass}
        topicStanceRecords={key=topicId+topicStanceId value=TopicStanceClass}
    
    Loading from each sheet:
        for every row from sheet:
            object=*Model(.....)
            key=extract key from row
            *Records[key]=object
        
    
    
'''
class LoadInput:

    def __init__(self, filePath):
        self.authorSheet = pandas.read_excel(filePath, sheet_name="author")
        self.discussionSheet = pandas.read_excel(filePath, sheet_name="discussion")
        self.discussionStanceSheet = pandas.read_excel(filePath, sheet_name="discussion_stance")
        self.discussionTopicSheet = pandas.read_excel(filePath, sheet_name="discussion_topic")
        self.postSheet = pandas.read_excel(filePath, sheet_name="post")
        self.quoteSheet = pandas.read_excel(filePath, sheet_name="quote")
        self.topicSheet = pandas.read_excel(filePath, sheet_name="topic")
        self.topicStanceSheet = pandas.read_excel(filePath, sheet_name="topic_stance")
        #creating individual empty records
        self.authorRecords={}
        self.discussionRecords={}
        self.discussionStanceRecords={}
        self.discussionTopicRecords={}
        self.postRecords={}
        self.quoteRecords={}
        self.topicRecords={}
        self.topicStanceRecords={}




    def loadDataFromAllSheets(self):
        self.loadDataFromAuthorSheet()
        #call the  remaining loadDataFrom*Records()


#.............................................................................................................
    def loadDataFromAuthorSheet(self):
        for index, row in self.authorSheet.iterrows():
            if row[columnsToCheck].isnull().values.any() or (type(row['author_id']) == str and not row['auhtor_id'].isdigit()):
                continue
            k = (row['author_id'])
            key = str(k) 

            obj=Author(row['author_id'])
            self.authorRecords[key]=obj
        print(self.authorRecords)
#................................................................................................
    def loadDataFromDiscussionSheet(self):
        columnsToCheck = ['discussion_id', 'title', 'initiating_author_id']
        for index, row in self.discussionSheet.iterrows():
            if row[columnsToCheck].isnull().values.any() or (type(row['initiating_author_id']) == str and not row['initiating_author_id'].isdigit()):
                continue
            k = (row['discussion_id'], row['initiating_author_id'])
            key = str(k[0]) + '_' + str(k[1])

            obj=Discussion(row['discussion_id'], row['title'], row['initiating_author_id'])
            self.discussionRecords[key]=obj
        print(self.discussionRecords)
#.....................................................................................................
    def loadDataFromDiscussionStanceSheet(self):
        columnsToCheck = ['discussion_id', 'discussion_stance_id', 'discussion_stance']
        for index, row in self.discussionStanceSheet.iterrows():
            #here data is in good formate no need to check wheather the columns contain strings or not so 
            if row[columnsToCheck].isnull().values.any():
                continue
            k = (row['discussion_id'], row['discussion_stance_id'])
            key = str(k[0]) + '_' + str(k[1])

            obj= DiscussionStance(row['discussion_id'], row['discussion_stance_id'], row['discussion_stance'])
            self.discussionStanceRecords[key]=obj
        print(self.discussionStanceRecords)
#.....................................................................................................
    def loadDataFromdiscussionTopicSheet(self):
        columnsToCheck = ['discussion_id', 'topic_id']
        for index, row in self.discussionTopicSheet.iterrows():
            #here data is in good formate no need to check wheather the columns contain strings or not so 
            if row[columnsToCheck].isnull().values.any():
                continue
            k = (row['discussion_id'], row['topic_id'])
            key = str(k[0]) + '_' + str(k[1])

            obj= DiscussionTopic(row['discussion_id'], row['topic_id'])
            self.discussionTopicRecords[key]=obj
        print(self.discussionTopicRecords)
#.....................................................................................................
    def loadDataFromTopicSheet(self):
        columnsToCheck = ['topic_id', 'topic']
        for index, row in self.topicSheet.iterrows():
            #here data is in good formate no need to check wheather the columns contain strings or not so 
            if row[columnsToCheck].isnull().values.any():
                continue
            k = (row['topic_id'])
            key = str(k)

            obj= Topic(row['topic_id'], row['topic'])
            self.topicRecords[key]=obj
        print(self.topicRecords)
#.....................................................................................................
    def loadDataFromTopicStanceSheet(self):
        columnsToCheck = ['topic_id', 'topic_stance_id', 'stance']
        for index, row in self.topicStanceSheet.iterrows():
            #here data is in good formate no need to check wheather the columns contain strings or not so 
            if row[columnsToCheck].isnull().values.any():
                continue
            k = (row['topic_id'],row['topic_stance_id'])
            key = str(k[0]) + '_' + str(k[1])

            obj= TopicStance(row['topic_id'],row['topic_stance_id'],  row['stance'])
            self.topicStanceRecords[key]=obj
        print(self.topicStanceRecords)
#................................................................................
"""
    def loadDataFromPostSheet(self):
        columnsToCheck = ['discussion_id', 'author_id','post_id' 'response_type']
        for index, row in self.postSheet.iterrows():
            #here data is in good formate no need to check wheather the columns contain strings or not so 
            if row[columnsToCheck].isnull().values.any():
                continue
            k = (row['post_id'])
            key = str(k)

            obj= Post(row['discussion_id'], row['author_id'], row['post_id'],row['parent_post_id'] ,row['response_type'])
            self.postRecords[key]=obj
        print(self.postRecords)
Mainobject=LoadInput('C:/Users/vaishu/Desktop/Project/MPphase2/input/createdebate_released_no_parse.xlsx')
Mainobject.loadDataFromPostSheet()
#........................................................................................................
    def loadDataFromQuoteSheet(self):
        columnsToCheck = ['discussion_id', 'post_id', 'source_post_id']
        for index, row in self.quoteSheet.iterrows():
            if row[columnsToCheck].isnull().values.any():
                continue
            k = (row['post_id'], row['source_post_id'])
            key = str(k[0]) + '_' + str(k[1])

            obj=Quote(row['discussion_id'], row['post_id'], row['source_post_id'])
            self.quoteRecords[key]=obj
        print(self.quoteRecords)
#.............................................................................................................

"""



Mainobject=LoadInput('C:/Users/vaishu/Desktop/Project/MPphase2/input/createdebate_released_no_parse.xlsx')
"""Mainobject.loadDataFromAuthorSheet()
Mainobject.loadDataFromDiscussionSheet()
Mainobject.loadDataFromDiscussionStanceSheet()
Mainobject.loadDataFromPostSheet()
Mainobject.loadDataFromQuoteSheet()"""
