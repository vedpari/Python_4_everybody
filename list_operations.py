#looking inside list, use index operator
friends = ['Joseph','Glenn','Sally']
print(friends[1])

#Strings are not mutable.. For example
#...fruit = 'banana'
#...fruit[0]='b'
#We receive traceback error 'str' object does not support item assignment
#On the contrary, if a list with integers are present, items in the list can be changed. 
lotto = [2,14,26,41,63]
print(lotto)
lotto[2] = 28
print(lotto)

#Length of the list
greet = 'Hello Bob'
print(len(greet))
x = [1, 1.3, 'Joe', [1,2,3]]
print(len(x))

#Range function returns a list
print(range(4))
#output [0,1,2,3]
friends = ['Joseph','Glenn','Sally']
print(len(friends))
print(range(len(friends)))

#loop within loop
i = 0
for i in range(len(friends)) : 
	friend = friends[i]
	print('Happy New Year',friend)
	
#Adding 2 lists concatenates the 2 lists
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

#slicing upto but not including
t = [9,41,12,3,74,15]
print(t[1:3])

#Creating and appending a list
stuff = list() #This creates an empty list
stuff.append('book') #append function adds to the end of the list
stuff.append(99) #We could append to the list and modify the existing list(which cannot be done in strings), hence lists are mutable
print(stuff)
stuff.append('cookie')
print(stuff)

#in and not in operator
some = [1,9,21,10,16]
9 in some

#Lists orders are maintained. i.e what goes in first comes out first
friends = ['Joseph','Glenn','Sally']
friends.sort()
print(friends)

#Len min and max functions
nums = [3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#Calculating average 2 ways
#Method 1 - 
total = 0
count = 0
while True :
	inp = input("Enter a number:")
	if inp == 'done' : break
	value = float(inp)
	total = total + value
	count = count + 1
average = total/count
print('Average:',average)

#Method 2 - 
numlist = list() #Creating empty list
while True:
	inp2 = input('Enter a number:')
	if inp2 == 'done' : break
	value = float(inp2)
	numlist.append(value)
average2 = sum(numlist)/len(numlist)
print("Average:",average2)

#Split method looks for spaces in the string and stores the fragments in a list
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[1])

for w in stuff : 
	print(w)

#Split usually splits based on white spaces. But we can suggest the delimiters
line = 'first;;second;third'
thing = line.split(';')
print(thing)
