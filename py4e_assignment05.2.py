#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

#Desired output
#Invalid input
#Maximum is 10
#Minimum is 2

largest_num = None
smallest_num = None
while True :
	user_input_string = input("Enter a number:" ) 
	if user_input_string == 'done' :
		break
	try: 
		user_input_float = int(user_input_string)	
		if largest_num is None : 
			largest_num = user_input_float 
		elif user_input_float > largest_num : 
			largest_num = user_input_float
		if smallest_num is None : 
			smallest_num = user_input_float 
		elif user_input_float < smallest_num : 
			smallest_num = user_input_float
	except:
		print('Invalid input')
		continue
print('Maximum is', largest_num)
print('Minimum is', smallest_num)