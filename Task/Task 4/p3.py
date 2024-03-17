nested_list = [[1, 2, 3], [2, 3], [2, 4, 1]]

frequency = {}
for sublist in nested_list:
    if isinstance(sublist, list):
        for element in sublist:
            frequency[element] = frequency.get(element, 0) + 1
    else:
        frequency[sublist] = frequency.get(sublist, 0) + 1

print(frequency)