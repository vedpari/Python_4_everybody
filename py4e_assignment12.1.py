import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter -')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
resultsum = 0
list1 = list()
tags = soup('span')
sumElement = 0
for tag in tags:
	content = tag.contents[0]
	element = int(content.encode('utf-8'))
	sumElement = sumElement + element
print(sumElement)
