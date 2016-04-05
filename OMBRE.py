import urllib2
from bs4 import BeautifulSoup
import re
import os
from os.path import basename
from urlparse import urlsplit

url = 'http://theoatmeal.com/feed/random'


res = urllib2.urlopen(url)
html = res.read()
soup = BeautifulSoup(html, 'html.parser')
div = soup.find('div', {"id":"comic"})
#print div.prettify()


foldername = str(soup.head.contents[1].contents[0])
print foldername
folder_loc = '/home/shaurya/Downloads/Comics/' + str(foldername)
os.makedirs(folder_loc)
os.chdir(folder_loc)
imgs = div.find_all('img')
for image in imgs:
	#print image.get('src')
	imgUrl = str(image.get('src'))
	try:
		
		imgData = urllib2.urlopen(imgUrl).read()
		fileName = basename(urlsplit(imgUrl)[2])
		#print fileName
		output = open(fileName,'wb')
		output.write(imgData)
		output.close()
	except:
		pass


os.remove('follow_fb.png')
os.remove('follow_google.png')
os.remove('follow_twitter.png')