def solve(matrix):
    pairs= []
    m = len(matrix)
    n = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                pairs.append([i,j])


    for pair in pairs:
        for i in range(n):
            matrix[pair[0]][i] = 0
        for j in range(m):
            matrix[j][pair[1]] = 0

    return matrix


if __name__ == '__main__':
    result = solve(matrix = [[1],[0]])
    print(result)