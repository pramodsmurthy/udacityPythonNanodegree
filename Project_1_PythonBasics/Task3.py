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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def findAreaCodeAndPrefix(calls):
	index = 0	
	bangaloreAreaCode = "(080)"
	mobileNumStart = ["7", "8", "9"]
	areaCodesAndPrefixes = []
	callerFromBangalore = 0
	receiverFromBangaloreFixed = 0
	assert( len(calls[0]) > 0 )
	while index < len(calls):
		caller = calls[index][0].lstrip()
		receiver = calls[index][1].lstrip()

		# Check if caller is from bangalore fixed line
		if caller[:5] == bangaloreAreaCode:
			callerFromBangalore += 1
			
			# Check if receiver is a fixed line			
			if bangaloreAreaCode[:2] == receiver[:2]:				
				# Receiver is a fixed line number
				ind = 2
				while ind < len(receiver) and receiver[ind] != ")":
					ind += 1
				if (ind == len(receiver)): print ("Error!! Unable to get prefix from number")
				prefix = receiver[:ind+1]
				if prefix not in areaCodesAndPrefixes:
					areaCodesAndPrefixes.append(prefix)					
			
			# Check if receiver is a mobile number
			if receiver[0] in mobileNumStart and receiver[5] == " ":
				if receiver[:4] not in areaCodesAndPrefixes:
					# Add mobile number prefix to our list					
					areaCodesAndPrefixes.append(receiver[:4])
			
			# Check if receiver is a fixed line from Bangalore
			if receiver[:5] == bangaloreAreaCode:
				receiverFromBangaloreFixed += 1
		
		index += 1
	print("The numbers called by people in Bangalore have codes:")	
	for num in sorted(areaCodesAndPrefixes):
		print(num)
	#print("{0} callers from bangalore and {1} receivers of fixed lines from bangalore".format(callerFromBangalore, receiverFromBangaloreFixed))
	print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format( ( receiverFromBangaloreFixed * 100.0 ) / callerFromBangalore) )

findAreaCodeAndPrefix(calls)

"""
O(n) for scanning through each entry in calls list.
Assuming a max prefix length of 6, 5 comparison operations are required to identify prefix for each number.
O(n) for scanning through selected list of numbers and logn (assuming) for in-built sort routine.
Total Time Complexity = O(n) + logn + O(n)= 2*O(n) + logn = O(n) + logn
Total Space Complexity = O(n). O(n) for storing selected list of numbers, few local variables which has O(1). 
"""