def odd_Sum(lst):
    sum = 0
    for num in lst:
        if num % 2 != 0:
            sum += num
    return sum

numbers = list(map(int, input("Enter a list of numbers: ").split()))
res = odd_Sum(numbers)
print("Sum of odd numbers:", res)
