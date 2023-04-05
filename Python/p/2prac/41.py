def mult_matrix(first_matrix, second_matrix):
    res = first_matrix
    for i in range(len(first_matrix)):
        for j in range(len(first_matrix[i])):
            res[i][j] = first_matrix[i][j] * second_matrix[i][j]
    return res


print(mult_matrix([[0, 2], [3, 0]], [[1, 4], [2, 0]]))
