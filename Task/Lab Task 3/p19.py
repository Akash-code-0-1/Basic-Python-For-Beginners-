""" 
Given a list of integers, write a Python program to create a new list that contains only the even numbers from the original list.

"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)