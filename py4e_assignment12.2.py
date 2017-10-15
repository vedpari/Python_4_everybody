import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count - ')
position = input('Enter position - ')

html1 = urllib.request.urlopen(url, context=ctx).read()
soup1 = BeautifulSoup(html1, 'html.parser')


final_list = list()
position = int(position) - 1
# Retrieve all of the anchor tags
tags1 = soup1('a')
for tag in tags1:
	emailId1 = tag.get('href', None).split()
	for email in emailId1:
		if position == 3:
			final_list.append(email)
		position = position + 1
print(final_list)


html2 = urllib.request.urlopen(final_list[0], context=ctx).read()
soup2 = BeautifulSoup(html2, 'html.parser')
tags2 = soup2('a')
position = 1
for tag in tags2:
	emailId2 = tag.get('href', None).split()
	for email in emailId2:
		if position == 3:
			final_list.append(email)
		position = position + 1
print(final_list)