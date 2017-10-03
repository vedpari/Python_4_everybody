#looping through strings

#**** Way 1 ****: 
#fruit = 'banana'
#index = 0 
#while index < len(fruit):
#	letter = fruit[index]
#	print(index,letter)
#	index = index + 1

# **** Way 2 ****: 
#fruit = 'banana'
#index = 0
#for letter in fruit:
#	print(index,letter)
#	index = index + 1

# How many 'a' in the letter
#fruit = 'banana'
#count = 0
#for letter in fruit:
#	if letter == 'a':
#		position = pos(fruit)
#		count = count + 1
#		print (position, count)
		
#in is also used as logical operator and it results in boolean value. 
#for example
#fruit = 'banana'
#'n' in fruit 
#True
 
# String comparison
#Upper case letters are smaller than lower case letters i.e A<a
#capitalize makes the first character capital. 

#find function is used for searching a substring & gives the position
pos = 0
fruit = 'banana'
pos = fruit.find('na')
print(pos)
 
