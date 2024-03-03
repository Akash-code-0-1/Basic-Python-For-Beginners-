"""
Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
"""

myList=[]

for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        myList.append(str(x))

print(','.join(myList)) # ','.join(listName) it add a comma between numbers