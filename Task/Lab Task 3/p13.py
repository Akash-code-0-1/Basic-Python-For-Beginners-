""" 
Given a list of integers, write a Python program using a for loop to find the su m, average, maximum, and minimum values in the list.

"""

numbers = [5, 10, 15, 20, 25]

total_sum = sum(numbers)
average = total_sum / len(numbers)
maximum_value = max(numbers)
minimum_value = min(numbers)

print(f"Sum: {total_sum}")
print(f"Average: {average}")
print(f"Maximum value: {maximum_value}")
print(f"Minimum value: {minimum_value}")