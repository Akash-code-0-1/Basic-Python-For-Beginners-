def sum_of_digits(digits):
    if digits<1:
        return digits
    return digits % 10 + sum_of_digits(digits//10)

N=int(input("Enter a Number: "))
print("Digits Sum=", sum_of_digits(N))