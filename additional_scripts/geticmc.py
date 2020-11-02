from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def getPageHtmlSourceCode(url):
	try: 
		f = urlopen(url)
		pageContent = BeautifulSoup(f.read(), "html.parser")
		return pageContent
	except: 
		return "error"

def inputUrl():
	url = "https://quod.lib.umich.edu/i/icmc/bbp2372.*"
	htmlSourceCode = getPageHtmlSourceCode(url);
	if htmlSourceCode !="error":
		return htmlSourceCode
	print("\nCouldn't connect to the web, please check the url entered or try again later\n")

def getYearUrls():
	yearPage = inputUrl()

	regexp = re.compile("bbp2372")

	yearUrls=[]
	for link in yearPage.find_all('a'):
		if link.has_attr('href'):
			result = regexp.search(link['href'])
			if result:
				yearUrls.append(link['href'])
	return yearUrls

# return a list of urls to individual pdfs on year page
def getPdfsByYear(url):
	htmlSourceCode = getPageHtmlSourceCode(url)
	regexp = re.compile("/bbp2372\.....\..../")

	paperUrls=[]
	for link in htmlSourceCode.find_all('a'):
		if link.has_attr('href'):
			result = regexp.search(link['href'])
			if result:
				paperUrls.append(link['href'])
	return paperUrls



def dostuff():

	# returns the page for each year
	yearUrls = getYearUrls()

	# for year in yearUrls: 
	# 	print("\nShowing links for each paper by year")
	# 	paperUrls = getPdfsByYear(year)
	# 	print(paperUrls)
		
	# 	for paperUrl in paperUrls: 
	# 		htmlSourceCode = getPageHtmlSourceCode(year)
	# 		print("Getting page: " + paperUrl)

	# 		paperPage = getPageHtmlSourceCode(paperUrl)

	# 		regexp = re.compile("format=pdf")

	# 		for link in paperPage.find_all('a'):
	# 			if link.has_attr('href'):
	# 				result = regexp.search(link['href'])
	# 				if result: 
	# 					linkToPaper = "https://quod.lib.umich.edu" + link['href']
	# 					print("link to paper: " + linkToPaper)
	# 					paper = urlopen(linkToPaper)
	# 					data = paper.read()
	# 					s = re.split('/|\?|;|\.',linkToPaper)
	# 					filename = s[14]+'_'+s[15]+'_'+s[10]+'.pdf'
	# 					print("Saving file: " + filename)
	# 					file_ = open(filename, 'wb')
	# 					file_.write(data)
	# 					file_.close

	# print(i)
	for i in range(0,len(yearUrls)-1):
	# for i in range(26,len(yearUrls)-1):
	# for i in range(40,41):
		# print(i)
		# print(getYearUrls()[i])
		year = getYearUrls()[i]
		print("\nShowing links for each paper by year")
		paperUrls = getPdfsByYear(year)
		print(paperUrls)

		print("Year number: " + str(i))
		print(year)

		for paperUrl in paperUrls: 
			htmlSourceCode = getPageHtmlSourceCode(year)
			print("Getting page: " + paperUrl)

			paperPage = getPageHtmlSourceCode(paperUrl)

			regexp = re.compile("format=pdf")

			for link in paperPage.find_all('a'):
				if link.has_attr('href'):
					result = regexp.search(link['href'])
					if result: 
						linkToPaper = "https://quod.lib.umich.edu" + link['href']
						print("link to paper: " + linkToPaper)
						paper = urlopen(linkToPaper)
						data = paper.read()
						s = re.split('/|\?|;|\.',linkToPaper)
						filename = s[14]+'_'+s[15]+'_'+s[10]+'.pdf'
						print("Saving file: " + filename)
						file_ = open(filename, 'wb')
						file_.write(data)
						file_.close


dostuff()


