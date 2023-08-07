def print_matrix_integer(matrix):
    final=' '
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==len(matrix[i]):
                final=''
            print('{:d}{}'.format(matrix[i][j]),final,end="")
        print(end='\n')
'''matrix=[[1,2,3],[4,5,6],[7,8,9]]
print_matrix_integer(matrix)'''