dicco= {}
size = int(input("Enter Size:"))
for i in range(size ):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dicco[key] = value
print()   
for key, element in dicco.items():
    print(f"{key} : {element}" )
    