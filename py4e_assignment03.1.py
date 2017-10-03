# Desired output = 498.75

hrs = input("Enter Hours:")
rph = input("Enter Rate per hour:")
try: 
	float_hours = float(hrs)
	float_rate_per_hour = float(rph)
except:
	print("Error, please enter integer digits")
	quit()
pay = 0
if float_hours > 40 : 
	pay = (float_hours - 40) * (float_rate_per_hour * 1.5)
	pay = pay + (40 * float_rate_per_hour)
else :
	pay = pay + (float_hours * float_rate_per_hour)
print(pay)
