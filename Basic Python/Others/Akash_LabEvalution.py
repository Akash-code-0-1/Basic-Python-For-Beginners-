Names=["Akash", "Tanvir","Siam"]
AnotherNameList=[]
counter=0
for word in Names:
    counter+=1
    AnotherNameList.append(word)
    n=len(word)
    for character in range(n-1,-1,-1):
        print(word[character])
    print("Printed Characters of Word  ", counter)
print("Printing Another List:")
for word in AnotherNameList:
    print(word)