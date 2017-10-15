# Desired output
#Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
#Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
#Retrieved 4189 characters
#Count: 50
#Sum: 2...

import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

#count = 0


address = input('Enter location: ')
# if len(address) < 1: break

print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')
	
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
print('Count:',len(results))
tot = 0
for item in results:
	# print(item.find('count').text)
	tot += int(item.find('count').text)
print('Sum:', tot)