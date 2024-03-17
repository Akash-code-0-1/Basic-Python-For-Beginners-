def transpose_matrix(matrix):
    tm = []
    for i in range(len(matrix)):
        newList = []
        for j in range(len(matrix[i])):
            newList.append(matrix[j][i])
        tm.append(newList)
    print(tm)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose_matrix(matrix)
