def print_matrix_integer(matrix):
    print(matrix)
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for j in range(len(matrix)):
    for i in range(len(matrix)):
        print('{:d} '.format(matrix[i][j]), end="")
    print('\n')
    