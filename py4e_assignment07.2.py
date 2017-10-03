#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

#Desired output:
#Average spam confidence: 0.750718518519

fname = input("Enter file name: ")
fh = open(fname)
count = 0
pos = 0
totsum = 0
for line in fh:
	if line.startswith("X-DSPAM-Confidence:"): 
		count = count + 1
		pos = line.find('.')
		desiredoutput_infloat = float(line[pos-1:])
		totsum = totsum + desiredoutput_infloat
		#print(desiredoutput_infloat)
print(totsum/count)
print("Done")
