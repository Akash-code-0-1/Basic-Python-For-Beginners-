UniqueNumbers = list(map(int, input("Enter a list of unique Numbers: ").split()))

min_value = min(UniqueNumbers)
max_value = max(UniqueNumbers)

min_index = UniqueNumbers.index(min_value)
max_index = UniqueNumbers.index(max_value)

UniqueNumbers[min_index], UniqueNumbers[max_index] = max_value, min_value

print("After swapping minimal and maximal elements:", UniqueNumbers)
