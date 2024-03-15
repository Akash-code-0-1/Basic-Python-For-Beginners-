""" 
Write a Python program to remove duplicates from a given list while preserving the order of the elements.
"""

numbers = [1, 2, 3, 2, 4, 5, 1, 3]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List with duplicates removed:", unique_numbers)