"""

2.Type Conversion: Given a list of integers, write a Python program to convert each element of the list to a string.

"""

numbers=[23,45,56,56,23,456,234,45]
convertedString=list(map(str,numbers))
print(convertedString)

#alternative
numbers=[23,45,56,56,23,456,234,45]
newString=[str(i) for i in numbers]
print(newString)