#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

#Desired output:
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

handle = open('romeo.txt','r')
content = handle.read()
wordlist = list()
wordstr = None
for line in content:
	line = line.rstrip()
Linecontent = content.split()
for wordstr in Linecontent:
	if wordstr not in wordlist:
		wordlist.append(wordstr)
	wordlist.sort()
print(wordlist)

