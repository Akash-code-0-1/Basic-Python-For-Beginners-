def sum_of_Digits(n):
    if n==0:
        return 0
    return n%10 + sum_of_Digits(n//10)
    

num=int(input("Enter a Number: "))

res=sum_of_Digits(num)
print(res)

