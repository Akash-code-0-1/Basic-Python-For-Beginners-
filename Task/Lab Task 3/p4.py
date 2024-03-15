""" 
Write a Python function to check if a given string is a palindrome or not.
"""
def is_palindrome(string):
    return string == string[::-1]

userString=input("Enter a String: ")
if is_palindrome(userString):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
