"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from datetime import datetime
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def getDateTime(dateStr):
	if dateStr[2] == "/":
		datetimeobj = datetime.strptime(dateStr, "%d/%m/%Y %H:%M")
	else:
		datetimeobj = datetime.strptime(dateStr, "%d-%m-%Y %H:%M:%S")
	return datetimeobj.strftime("%B"), datetimeobj.strftime("%Y")

def findLongestTime(callData):
	assert(len(callData[0]) > 0)
	longest = int(callData[0][3])
	longestIndex = 0
	count = 1
	while count < len(callData):
		if (int(callData[count][3]) > longest):
			longest = int(callData[count][3])
			longestIndex = count
		count += 1
	mon, year = getDateTime(callData[longestIndex][2])
	print("{0} spent the longest time, {1} seconds, on the phone during {2} {3}".format(callData[longestIndex][0], callData[longestIndex][3], mon, year))

findLongestTime(calls)

"""
Time Complexity:	
O(n) for iterating all the elements (while loop). Constant time for finding date and time of longest call.
Time Complexity = O(n)
"""