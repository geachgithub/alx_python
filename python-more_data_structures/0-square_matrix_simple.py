def square_matrix_simple(matrix):
    squared=[]
    transposed=[]
    for i in range(len(matrix)):
        squared.append([row[i]**2 for row in matrix])   
    for i in range(len(matrix)):
        transposed.append([row[i] for row in squared])         
    '''print(len(matrix))
    print(matrix)
    print(squared)
    print(transposed)
matrix=[[1,2,3],[4,5,6],[7,8,9]]
square_matrix_simple(matrix)'''