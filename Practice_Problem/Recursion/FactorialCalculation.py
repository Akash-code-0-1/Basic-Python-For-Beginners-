def calculate_Facto(n):
    if n==0:
        return 1
    return n*calculate_Facto(n-1)


N=int(input("Enter a Number: "))
print("Factorial= ",calculate_Facto(N))