List = list(map(int, input("Enter a list of numbers: ").split()))

for i in range(0, len(List) - 1, 2):
    temp = List[i]
    List[i] = List[i + 1]
    List[i + 1] = temp

print("After swapping adjacent items:", List)
