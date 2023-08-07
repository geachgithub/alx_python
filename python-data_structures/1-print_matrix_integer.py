def print_matrix_integer(matrix):
    c=0
    for i in range(len(matrix)):
        final=' '
        for j in range(len(matrix[i])):
            c+=1
            if c==len(matrix[i]):
                final=''
            print('{:d}'.format(matrix[i][j]),end=final)
        print(end='\n')
'''matrix=[[1,2,3],[4,5,6],[7,8,9]]
print_matrix_integer(matrix)'''