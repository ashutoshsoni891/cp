def getPairs(matrix, m ,n):

    i = 0
    j = 0
    pairs= []
    while i <= m and j <=n:
        if(matrix[i][j] == 0):
            pairs.append([i, j])
        if(i == m-1 and j == n-1):
            break
        if (j == n-1):
            j = 0
            i += 1
        else:
            j += 1

    return pairs


def solve(matrix):
    m = len(matrix)
    n = len(matrix[0])
    pairs = getPairs(matrix, m, n)
    p = len(pairs)
    pairI = 0
    pairJ = 0
    i = 0
    j = 0

    #for row
    while pairI < p:

        matrix[pairs[pairI][0]][i] = 0
        i += 1

        if(i == n):
            pairI += 1
            i = 0

    #for col
    while pairJ < p:

        matrix[j][pairs[pairJ][1]] = 0
        j += 1

        if(j == m):
            pairJ += 1
            j = 0


    return matrix


if __name__ == '__main__':
    #o(mn) -> o(m +n)
    result = solve(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])
    print(result)