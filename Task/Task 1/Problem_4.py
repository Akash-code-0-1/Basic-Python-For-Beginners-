strings = input("Enter a list of strings: ").split()

count = 0
for string in strings:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

print("Result:", count)
