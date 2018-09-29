## Multiplication of two matrix

matrix1 = [[1, 2],
               [3, 4]]

matrix2 = [[1, 0],
               [0, 1]]

matrix = [[0, 0],
              [0, 0]]

## iterate through rows of matrix1
for i in range(len(matrix1)):
    ## iterate through colums of matrix2
    for j in range(len(matrix2[0])):
        ## iterate through rows of matrix2
        for k in range(len(matrix2)):
            matrix[i][j] += matrix1[i][k]*matrix2[k][j]

print(matrix)
