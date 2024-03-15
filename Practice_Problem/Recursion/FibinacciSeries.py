def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

N=int(input("Enter No. of Term: "))
for i in range(N):
    print(fibonacci(i), end=" ")