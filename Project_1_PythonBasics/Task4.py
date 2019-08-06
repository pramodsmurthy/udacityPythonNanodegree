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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def searchNum(numlist, num, column):
	num = num.strip()
	for row in numlist:
		if num == row[column].strip():
			return True
	return False

def findSpammers(calls, texts):
	index = 0
	potentialSpam = []
	while index < len(calls):
		num = calls[index][0]		
		if (searchNum(calls, num, 1) or searchNum(texts, num, 0) or searchNum(texts, num, 1)) is False:
			if num not in potentialSpam:				
				potentialSpam.append(num)
		index += 1	
	print("These numbers could be telemarketers: ")
	for num in sorted(potentialSpam):
		print(num)	

def test():
	with open("calls2.csv", "r") as f:
		reader = csv.reader(f)
		calls = list(reader)
	with open("texts2.csv", "r") as f:
		reader = csv.reader(f)
		texts = list(reader)
	findSpammers(calls, texts)

findSpammers(calls, texts)
#test()

"""
For each entry in caller list(of size n), we are performing a search 3 times. Each search will do a n element search. So for one entry in record, we will do a (n+n+n=3n) search.
So, for n elements, 3n + 3n + 3n + ..... + 3n = 3n (1+2+...+n) = 3n * (n * (n + 1 ) ) / 2 = 3n * n^2 = 3n^3 = O(n^3)
Space Complexity = O(n) to store the list of potential spammers.
"""


