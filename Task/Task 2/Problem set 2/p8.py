def sum_Of_Digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_Of_Digits(n // 10)


number = int(input("Enter a Number: "))
result = sum_Of_Digits(number)
print("Sum of digits:", result)


