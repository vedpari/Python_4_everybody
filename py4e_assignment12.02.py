import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


inp_url = input('Enter the url -')
inp_count = int(input('Enter count - '))
inp_position = int(input('Enter position - '))
urlList = list()

urlToFollow = inp_url

count = 0
while count <= inp_count:
	print("Retrieving: " + urlToFollow)
	urlList.append(urlToFollow)
	html = urllib.request.urlopen(urlList[count], context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	position = 0
	for tag in tags:
		if position == inp_position - 1:
			tempUrlList = tag.get('href', None).split()
			urlToFollow = tempUrlList[0]
		position = position + 1
	count = count + 1



	
