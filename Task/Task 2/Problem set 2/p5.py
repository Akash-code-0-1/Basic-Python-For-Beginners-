def palindromeCheck(mystring):
    return mystring == mystring[::-1]

mystring = input("Enter a string: ")
if palindromeCheck(mystring):
    print("Palindrome")
else:
    print("Not Palindrome")