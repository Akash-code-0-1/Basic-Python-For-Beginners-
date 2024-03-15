""" 
Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.
"""

limit = int(input("Enter Fibonacci sequence Limit: "))
a, b = 0, 1

for _ in range(limit):
    print(a, end=" ")
    a, b = b, a + b