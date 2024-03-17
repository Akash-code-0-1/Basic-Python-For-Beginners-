# Creating a set and a dictionary
my_set = {1, 2, 3, 4, 5}
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Similarities:
# 1. Membership testing
print(2 in my_set)   # Output: True
print('b' in my_dict)   # Output: True

# Differences:
# 1. Purpose and Usage
# Adding duplicate value to set
my_set.add(5)  # No change since sets do not allow duplicates
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Accessing value by key in dictionary
print(my_dict['a'])  # Output: 1

# Syntax
# Creating a set
another_set = {5, 6, 7, 8, 9}

# Creating a dictionary
another_dict = {'x': 10, 'y': 20, 'z': 30}

# Accessing elements
for element in another_set:
    print(element)  # Output: 5, 6, 7, 8, 9

for key in another_dict:
    print(key, another_dict[key])  # Output: x 10, y 20, z 30
