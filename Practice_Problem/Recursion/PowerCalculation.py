def power(base, p):
    if p==0:
        return 1
    return base* power(base,p-1)

print(power(2,3))