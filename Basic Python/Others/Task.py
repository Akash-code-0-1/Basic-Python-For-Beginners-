row = 3
column = 4
py2Dlist = []

print("Enter values for a", row, "x", column, "matrix:")

for i in range(row):
    inner_list = []
    for j in range(column):
        value = int(input(f"Enter value at position ({i+1},{j+1}): "))
        inner_list.append(value)
    py2Dlist.append(inner_list)

print("\n2D List:")
for row in py2Dlist:
    print(row)