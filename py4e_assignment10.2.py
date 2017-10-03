# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
handle = open(name)
lst = list()
counts = dict()
for line in handle:
	line = line.rstrip()
	if line.startswith('From'):
		splitting = line.split()
		if len(splitting) >= 6:
			elem = splitting[5]
			# print (elem)
			hour = elem.split(':')
			hour_element = hour[0]
			counts[hour_element] = counts.get(hour_element,0) + 1
#print(counts)
for k,v in counts.items():
	lst.append((k,v))
lst = sorted(lst) 
for k,v in lst:
	print(k,v)


