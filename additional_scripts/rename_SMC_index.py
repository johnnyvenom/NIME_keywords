import os
from natsort import natsorted, ns

path = "/Users/johnnyvenom/Documents/Projects/DMI-lit-review/SMC/"
yearSubdirs = os.listdir(path)
yearSubdirs = natsorted(yearSubdirs, alg=ns.IGNORECASE)

for yearDir in yearSubdirs: 
	
	yearPath = path+yearDir+'/'
	conf,year = yearDir.split("_") 

	print(year)
	print(yearPath)

	files = os.listdir(yearPath)
	files = natsorted(files, alg=ns.IGNORECASE)
	# print(files)


	i = 1

	for file in files:
		filename, file_extension = os.path.splitext(file)
		filename = filename.replace(" ", "_")
		# print(os.rename(os.path.join(yearPath, file)))
		os.rename(os.path.join(yearPath, file), os.path.join(yearPath, year + "_" + format(i, '03') + "_" + filename + file_extension))
		i = i + 1
		
		

