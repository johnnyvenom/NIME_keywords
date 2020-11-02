import os
from shutil import copyfile

basePath = "/Users/johnnyvenom/Documents/Projects/DMI-lit-review/NIME/"

yearDirs = os.listdir(basePath)
print(yearDirs)

for yearDir in yearDirs:
	files = os.listdir(basePath+yearDir)

	for paper in files: 
		year = paper[:4]

		targetDir = basePath[:-5] + "corpus/NIME/" + year
		if not os.path.exists(targetDir):
			os.mkdir(targetDir)


		oldFilePath = basePath + yearDir + "/" + paper
		newFilePath = targetDir + "/NIME_" + paper
		copyfile(oldFilePath, newFilePath)
		print("Added: " + newFilePath)



