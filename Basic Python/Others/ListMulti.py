# Sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]

# Multiply the elements and store the results in a new list
result_list = [x * y for x, y in zip(list1, list2)]

# Print the result
print(result_list)