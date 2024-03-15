""" 
Write a Python program using a while loop to count the number of digits in a given integer N.
"""

N = int(input("Enter an integer: "))
count = 0

while N != 0:
    N //= 10
    count += 1

print("Number of digits:", count)