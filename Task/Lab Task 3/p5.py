""" 
Write a Python function to reverse a given string using slicing.
"""
def stringReverse(s):
    return s[::-1]

string=input("Enter a String:")
reversed_string = stringReverse(string)
print("Reversed string:", reversed_string)