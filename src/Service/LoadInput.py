import pandas


'''
    Format:
        authorRecords ={ key=authorId ,value=AuthorClass}
        discussionRecords={key=discussionId value=DiscussionClass}
        discussionStanceRecords={key =discussion_id+discussion_stance_id value=DiscussionStanceClass}
        discussionTopicRecords={key=discussionId+topicId value=DiscussionTopicClass}
        postRecords={key=discussionId+postId value=PostClass}
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

    def __int__(self, filePath):
        self.authorSheet = pandas.read_excel(filePath, sheet_name="author")
        self.discussionSheet = pandas.read_excel(filePath, sheet_name="discussion")
        self.discussionStanceSheet = pandas.read_excel(filePath, sheet_name="discussion_stance")
        self.discussionTopicSheet = pandas.read_excel(filePath, sheet_name="discussion_topic")
        self.postSheet = pandas.read_excel(filePath, sheet_name="post")
        self.quoteSheet = pandas.read_excel(filePath, sheet_name="quote")
        self.topicSheet = pandas.read_excel(filePath, sheet_name="topic")
        self.topicStanceSheet = pandas.read_excel(filePath, sheet_name="topic_stance")
        self.authorRecords=None
        self.discussionRecords=None
        #remaining Vaishu



    def loadDataFromAllSheets(self):
        self.loadDataFromAuthorSheet()
        #call the  remaining loadDataFrom*Records()



    def loadDataFromAuthorSheet(self):
        pass











