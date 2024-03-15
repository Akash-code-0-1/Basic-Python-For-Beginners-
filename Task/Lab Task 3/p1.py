"""
1.	String Reverse: Write a Python function to reverse a given string and return the reversed string. 
"""
givenString=input("Enter Your Name: ")
finalString=givenString[::-1]
print(finalString)



#another solution
for char in reversed(givenString):
    print(char,end='')