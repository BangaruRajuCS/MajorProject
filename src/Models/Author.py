import pandas
# import glob
class Author:
	def __init__(self):
		#directory_path = 'C:\\Users\\vaishu\\Desktop\\Project\\MPphase2\\input'
		#Retriving Author datasheet from createdebate execel 
		authorSheet = pandas.read_excel('createdebate_released_no_parse.xlsx', sheet_name='author')
        # Retiving particular coloumn form the sheet
		self.__authorId = authorSheet['author_id']
	#get and set function for author id variable
	def get_authorID(self):
		return self.__authorId
	def set_authorId(self,value):
		self.__authorId=value
#create an object to the author Class
obj=Author()
#use the getter methods to acccess the private variables
print(obj.get_authorID())

