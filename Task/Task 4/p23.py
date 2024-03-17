def dict(L):
    sd = {}
    for num in L:
        key=num
        value=num**2
        sd[key]=value
    return sd

L= [1, 2, 3, 4, 5]

newdict= dict(L)

for key, value in newdict.items():
    print(f"{key}: {value}")