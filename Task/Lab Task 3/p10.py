""" 
Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user

"""
N = int(input("Enter a number: "))
sum_even = 0
i = 2

while i <= N:
    sum_even += i
    i += 2

print("Sum of even numbers:", sum_even)