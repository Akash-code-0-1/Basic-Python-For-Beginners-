def addMatrix(m1,m2):
    result=[]
    for i in range(len(matrix1)):
        add=[]
        for j in range(len(matrix1[i])):
            add.append(matrix1[i][j]+matrix2[i][j])
        result.append(add)
    return result


matrix1=[[1,3,5],[2,3,5],[5,6,7]]
matrix2=[[3,4,5],[2,4,5],[1,3,4]]

print(addMatrix(matrix1,matrix2))