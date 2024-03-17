def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Create a list of integers from 1 to 100
numbers = list(range(1, 101))

# Use filter function to keep only prime numbers
prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers from 1 to 100:")
print(prime_numbers)
