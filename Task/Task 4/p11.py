t = (34, 67, 34, 23, 45, 345, 1, 3, 5, 234, 56)
newt = ()
index = len(t) - 1

while index >= 0:
    newt += (t[index],)
    index -= 1

print(newt)
