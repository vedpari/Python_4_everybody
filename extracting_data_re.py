import re

name = input("Enter file:")
handle = open(name)
lst = list()
results = list()
results_sum = 0
total = 0 
for line in handle:
	line = line.rstrip()
	y = re.findall('[0-9]+',line)
	if len(y) > 0:
		results = list(map(int,y))
		for result in results:
			results_sum = results_sum + result
print(results_sum)
		