def square_matrix_simple(matrix):
    squared=[]
    transposed=[]
    m=0
    for i in range(len(matrix[m])):
        squared.append([row[i]**2 for row in matrix])   
        m+=1
    for i in range(len(matrix)):
        transposed.append([row[i] for row in squared]) 

    '''#return(transposed)   
    print(len(matrix))
    print(matrix)
    print(squared)
    print(transposed)
matrix=[[1,2],[4,5],[7,8]]
square_matrix_simple(matrix)'''