def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_natural_numbers(n - 1)


print(sum_of_natural_numbers(5)) 