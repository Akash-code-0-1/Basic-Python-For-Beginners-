m = int(input("Enter Size of String: "))
userString= input("Input String: ")
n = int(input(" Enter Number of characters to rotate: "))

finalString = userString[n:] + userString[:n]

print("Rotated String is:", finalString)