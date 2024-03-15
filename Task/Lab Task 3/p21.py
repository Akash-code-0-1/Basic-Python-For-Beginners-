""" 
Given two lists of integers, write a Python program to create a new list that contains elements common to both lists.
"""

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = [element for element in list1 if element in list2]
print("Common elements:", common_elements)