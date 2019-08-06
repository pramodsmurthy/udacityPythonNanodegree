"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def findUnique1(datalist, datalist1):
	assert(len(datalist[0]) > 0)
	uniqueRec = []
	count = 0
	lengthofbiglist = max(len(datalist), len(datalist1))
	while count < lengthofbiglist:
		if count < len(datalist):
			if datalist[count][0] not in uniqueRec:
				uniqueRec.append(datalist[count][0])
			if datalist[count][1] not in uniqueRec:
				uniqueRec.append(datalist[count][1])
		if count < len(datalist1):
			if datalist1[count][0] not in uniqueRec:
				uniqueRec.append(datalist1[count][0])
			if datalist1[count][1] not in uniqueRec:
				uniqueRec.append(datalist1[count][1])
		count += 1
	for num in uniqueRec:
		print(num)
	return len(uniqueRec)

print("There are {0} different telephone numbers in records".format(findUnique1(calls, texts)))

"""
Complexity:
Time Complexity = For each entry in caller list, n element search is performed 4 times, which is 4n. 
For n, elements time complexity = 4n + 4n + 4n+ ..... +4n = 4n (1+2+3+...+n) = 4n * (n*(n+1)/2) = 4n * n^2 = 4n^3 = O(n^3)
Space Complexity = O(n) for storing unique records, where n is the length of the largest record (either call or text).
"""
