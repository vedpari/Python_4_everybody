#Creating a new dictionary, adding new key-value pairs, comparing if the key is already present, incrementing the counter by 1.
#Program to know how many times the name has showed up. 

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
	if name not in counts:
		counts[name] = 1
	else:
		counts[name] = counts[name] + 1
print(counts)
	

#get method is used to check if the key is already present. And if it is not present, it defaults without throwing a traceback.
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
	counts[name] = counts.get(name,0) + 1
print(counts)

#Counting pattern
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()
print('Words:',words)
print('Counting....')
for word in words:
	counts[word] = counts.get(word,0) + 1
print('counts:', counts)
print(counts.keys()) #Just gives the keys in the list
print(counts.values()) #Just gets the values in the list
print(counts.items()) #Gets the list of key value pair in the list
for k,v in counts.items(): #Use of 2 iteration variables to go over key and value simultaneously
	print(k,v)

#Find the most used word from the file
name = input("Enter a file name:")
handle = open(name)

counts = dict()
for line in handle:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1
bigword = None
bigcount = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count
print(bigword,bigcount)