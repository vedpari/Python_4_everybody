#Using tuples, sorting takes place using the key. To get sorting on value:
c = {'a':10, 'b':1, 'c':22} #dictionary
tmp = list() #Creating a new list
for k,v in c.items():
	tmp.append((v,k)) #Append to the list the reverse of key and value
print(tmp) #this gives a list not in any specific order
tmp = sorted(tmp,reverse=True) #sorted sorts the list. reverse=True gives high to low
print(tmp)


#Problem of finding 10 most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1

lst = list()
for key,value in counts.items():
		newtup = (value,key)
		lst.append(newtup)
lst = sorted(lst, reverse=True)
for value,key in lst[:10]:
	print(key,value)
	
#Reversing and sorting (everything that is done in above code) can be done using the following line of code

fhandle = open('romeo.txt')
counts_dict = dict()
lst = list()
for line in fhandle:
	words = line.split()
	for word in words:
		counts_dict[word] = counts_dict.get(word,0) + 1
lst = sorted([(v,k) for k,v in counts_dict.items()],reverse=True) #This is called list comprehension
for i,j in lst[:10]:
	print(j,i)
	
