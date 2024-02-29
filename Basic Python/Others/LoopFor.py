'''
def forforrange1():
    print("Rnage(n)")
    for i in range(6):
        print(i)
    
def forforrange2():
    print("Rnage(1,n)")
    for i in range(1,6):
        print(i)
    

def forforrange3():
    print("Rnage(1,n,2)")
    for i in range(1,6,2):
        print(i)
    
    
def forforrange4():
    print("Rnage(6,1,-1)")
    for i in range(6,1,-1):
        print(i)
        
        


forforrange1()
forforrange2()
forforrange3()
forforrange4()

print("End of Function work")

n=12345668
n=str(n)
count=0

for i in n:
    count+=1
print(count)

student=[]
#student.append("Akash")
#student.append("Ahid")

i=0
n=int(input("Enter how many student you want to add: "))
while i<n:
    student.append(input("Enter Here: "))
    i=i+1
print("Thanks for Adding")
#print(student)
#student.insert(1,"Akash")

#print(student)

#student.pop(1)
#print(student)
student.reverse()
print(student)
student_id=[1,2,3]
student.extend(student_id)
print(student)

st=[]
st2=student.copy()
print(student)

'''

st3=[34,56,67,789,345,678,8,3]
st3.sort()
print(st3)

st4=["aksh", "siam","Ahid"]
st4.sort()
print(st4)

st4.clear()
print(st4)

print(st4.index("aksh"))
    



