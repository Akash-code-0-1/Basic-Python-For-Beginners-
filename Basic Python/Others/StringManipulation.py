"""n=int(input("Enter String Size: "))
myString=''
for i in range(1,n+1,1):
    x=input()
    if x!=' ':
        myString+=x
print(myString)
"""
myString = "AkashT"
counter = 0 

for i in range(len(myString)-3, len(myString)):
    counter += 1
    myString = myString[:i] + str(counter) + myString[i+1:]

print(myString)

specialChar = ["#", "@", "!"]

counter2 = 0
for i in range(3):  # Loop over the first three characters
    myString = specialChar[i] + myString[1:]  # Replace each character with the corresponding special character

myString=myString.upper
print(myString)

    




