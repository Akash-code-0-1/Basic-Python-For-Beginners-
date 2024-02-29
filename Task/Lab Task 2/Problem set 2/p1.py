def is_unique_number(n):
    num_str = str(n)
    if len(num_str) == len(set(num_str)):
        return n

numbers = list(map(int, input("Enter a list of Numbers: ").split()))

uniqueNumbers = []

for num in numbers:
    unique_num = is_unique_number(num)
    if unique_num is not None:
        uniqueNumbers.append(unique_num)

print("Unique Elements Are:", uniqueNumbers)
