from src.Service.LoadInput import LoadInput


filePath="/home/br/Desktop/projectPhase2/MajorProject/input/convinceme_no_parse.xlsx"

loadInput=LoadInput(filePath)
loadInput.loadDataFromAllSheets()
print(loadInput.authorRecords)