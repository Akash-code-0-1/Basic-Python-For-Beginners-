""" 
Write a Python program using a while loop to check if a given number N is prime or not.

"""

N = int(input("Enter a number: "))
is_prime = True

if N < 2:
    is_prime = False

i = 2
while i*i <= N:
    if N % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print(f"{N} is a prime number.")
else:
    print(f"{N} is not a prime number.")