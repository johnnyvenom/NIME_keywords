import os
from shutil import copyfile

basePath = "/Users/johnnyvenom/Documents/Projects/DMI-lit-review/"
conference = "ICMC"


# input list of papers to be included
fileRef = conference.lower() + "_corpus.txt"
file = open(fileRef, "r")
oldFileList = file.readlines() 

# strip newline characters where needed
fileList = []
for item in oldFileList: 
	if item[-1:] == "\n":
		item = item[:-1]
		fileList.append(item)

# copy paper from master directory to corpus directory
for paper in fileList: 
	year = paper[:4]

	if not os.path.exists(basePath+"corpus/"+conference+"/"+year):
		os.mkdir(basePath+"corpus/"+conference+"/"+year)

	oldFilePath = basePath + conference + "/" + year + "/" + paper
	newFilePath = basePath + "corpus/" + conference + "/" + year + "/" + conference + "_" + paper
	copyfile(oldFilePath, newFilePath)  
	print("Added: " + newFilePath)
