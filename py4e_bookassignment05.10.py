#Exercise 1: Write a program which repeatedly reads numbers until the user enters
#“done”. Once “done” is entered, print out the total, count, and average of the
#numbers. If the user enters anything other than a number, detect their mistake
#using try and except and print an error message and skip to the next number.


total = 0.0
count = 0
while True :
	user_input_string = input("Enter a number:" )
	if user_input_string == 'done' :
		break
	try: 
		user_input_float = float(user_input_string)
	except:
		print('Invalid input')
		continue

	count = count + 1
	total = total + user_input_float
print(total, count, total/count)