#Using re.search() like find()

#Without RE:
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.find('From:') >=0:
		print(line)
print('*********')
#Using RE:

import re #Import the RE library

hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('From:', line): #here From: is the string we are trying to search in line. re.search() returns a true or false
		print(line)
print('**********')

#Using re.search() like startswith()
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.startswith('From:'):
		print(line)
print('*************')

#Using RE:
import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^From:',line): #Making use of ^ searches for line starting with F. 
		print(line)	

		
# Wild card characters
# dot . -> character matches any character
# asterisk * -> any number of time
#For example ^X.*: -> All line starting with X and have any number of characters following it, until :
# ^X-\S+: -> \S is match any non white space character, + is one or more times
#[0-9]+ -> one or more digits. returns a list of the matches

import re
x = 'My 3 favorite numbers are 05,24 and 12 '
y = re.findall('[0-9]+',x)
print(y)
#result ['3','05','24','12']
z = re.findall('[AEIOU]+1',x) #Check to see if there are any uppercase AEIOU
print(z)
#Result []

#Greedy: .* or .+ tries to get the largest chracters until the :
#To make it non greedy add ? For example: '^F.+?:'

#get email address
import re
x = 'From: cwen@iupui.edu Fri, 4 Jan 2008 18:08:57 -0500'
y = re.findall('\S+@\S+',x)
print(y)

#Fine tuning string extraction
import re
x = 'From cwen@iupui.edu Fri, 4 Jan 2008 18:08:57 -0500'
y = re.findall('^From (\S+@\S+)',x) #() are the start and end of extraction
print(y)
z = re.findall('@([^ ]*)',x)
print(z)