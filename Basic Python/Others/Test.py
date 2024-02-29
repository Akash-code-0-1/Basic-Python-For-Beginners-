n=[1,2,3,4,5,6,7,8,9]
List=[]
for x in n:
  x=x**2
  List.append(x)
  
print(List)

newList = [n[x]*n[x] for x in range(len(n)) if n[x] % 2 == 0]

print(newList)