def calculate_Fibo(n):
    if n<=1:
        return n
    return calculate_Fibo(n-1)+calculate_Fibo(n-2)

N=int(input("Enter a Number: "))
print("Fibonacci=", calculate_Fibo(N))