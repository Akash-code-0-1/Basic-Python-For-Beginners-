"""
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

"""

numbers=input("Input Some comma-seperaed numbers: ")
myList=numbers.split(",")
    
print("List:")
print(myList)

myTuple=tuple(myList)
print("Tuple:")
print(myTuple)