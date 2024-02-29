def positiveNumbers(numbers):
    for num in numbers:
        if num <= 0:
            continue
        print(num)

numbers = list(map(int, input("Enter a list of Numbers: ").split()))
print("Positive numbers Are:")
positiveNumbers(numbers)
