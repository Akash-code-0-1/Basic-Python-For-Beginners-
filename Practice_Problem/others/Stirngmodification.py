""" 
User
you should taka a string at m size without any space, where m>8 . now replace first 3 character of the string woth 3 digits , replace last 3 charactrs by special characters and leter should be uppercase . solve it in pyhton
"""


myString = input("Enter a string (string > 8 char) : ")

if len(myString) <= 8:
    print("Enter more than 8 character")
else:

    digits = "123"
    newstring = digits + myString[3:]

    special_chars = "#!@"
    newstring = newstring[:-3] + special_chars.upper()


    print("Modified string:", newstring.upper())
