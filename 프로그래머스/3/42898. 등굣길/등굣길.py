def solution(m, n, puddles):
    answer = 0
    coor = [[0]*(m+1) for _ in range(n+1)]

    for x, y in puddles:
        coor[y][x] = -1

    coor[1][0] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if coor[i][j] == -1:
                coor[i][j] = 0
            else:
                coor[i][j] = (coor[i-1][j] + coor[i][j-1]) % 1000000007

    answer = coor[n][m]
    return answer
