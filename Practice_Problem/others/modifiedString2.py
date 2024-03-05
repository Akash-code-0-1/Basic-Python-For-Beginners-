""" 
You are asked to take an input as string at 'm' size where m>=5 . Then, convert that string by applying following facts.....
1) Add some digitsat the end of that string as "1st" digit is the lenght of the input string & next of the digits will be the ASCII value of the first character
2) then, concatemate '@gmail.com' at the end of the output of above mentioned
3) Finally, print the resultant string

Sample input: Ayman
Sample Output: Ayman567@gmail.com
"""


myString = input("Enter a string (string >=5 char) : ")

if len(myString) < 5:
    print("Enter more than 5 or 5 character")
else:
    myString=myString+str(len(myString))+str(ord(myString[0]))+"@gmail.com"
    print(myString)



