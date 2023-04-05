def transpose(matrix):
    res = []
    for j in range(len(matrix[0])):
        tmp = []
        for i in range(len(matrix)):
            tmp += [matrix[i][j]]
        res += [tmp]
    return res


print(transpose([[0, 2, 1], [1, 0, 3], [0, 1, 1]]))