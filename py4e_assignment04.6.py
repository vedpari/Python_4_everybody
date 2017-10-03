#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

# Desired output = 498.75

hrs = input("Enter Hours:") 
rph = input("Enter Rate per hour:") 

try: 
	float_hours = float(hrs) 
	float_rate_per_hour = float(rph) 
except:
	print("Error, please enter integer digits")
	quit()
def computepay_overtime(hours, rate_per_hour): 
	pay = 0
	pay = (hours - 40) * (rate_per_hour * 1.5)  
	pay = pay + (40 * rate_per_hour) 
	return pay
	
def computepay(hours, rate_per_hour):
	pay = 0 
	pay = pay + (float_hours * float_rate_per_hour)
	return pay
	
if float_hours > 40 : 
	computepay_results = computepay_overtime(float_hours, float_rate_per_hour)
	
else :
	computepay_results = computepay(float_hours, float_rate_per_hour)
print(computepay_results)



