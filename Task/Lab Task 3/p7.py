""" 
 Write a Python program using a for loop to print the multiplication table of a given number N.
"""

N = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{N} x {i} = {N*i}")
    