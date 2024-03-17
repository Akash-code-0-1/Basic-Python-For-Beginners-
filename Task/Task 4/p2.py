def flatenList(L):
    newlist=[]
    for sublist in L:
        if isinstance(sublist,list):
            newlist.extend(flatenList(sublist))
        else:
            newlist.append(sublist)
    return newlist
    

nes_L=[[1,3,4,5],[3,5,6,7],[3.6,7,89,9]]
print(flatenList(nes_L))