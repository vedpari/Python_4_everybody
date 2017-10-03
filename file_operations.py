#Counting number of line
#handle = open('python_file.txt','r')
#count = 0
#for line in handle: 
#	count = count + 1
#print('Line Count:', count)

#Printing each line in the file
#file handle open() can be treated as sequence of strings where each line in the file is a string in the sequence. 

#handle = open('python_file.txt','r')
#for line in handle:
#	print(line)

#Getting characters from the file use read()
#handle = open('python_file.txt','r')
#inp = handle.read()
#print(len(inp))
#print(inp[:20])

#Searching through the file
#handle = open('python_file.txt','r')
#for line in handle :
#	if line.startswith('Completed'):
#		print(line)

#Print statement adds a new line.. So the output has 2 \n characters
#Eg: abcdefghi \ne
#\n
#asdfgh
handle = open('python_file.txt','r')
for line in handle:
	line = line.rstrip()
	print(line)