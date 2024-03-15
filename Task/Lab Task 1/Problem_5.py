items = map(str,input("Enter a list of Names: ").split())

lengths = []
for item in items:
    lengths.append(len(item))
print("Length of each item:", lengths)

converted_items = []
for item in items:
    converted_items.append(item.swapcase())
    
print("Converted items:", converted_items)

