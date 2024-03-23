def solution(n, m, board):
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == '-':
                if j == 0 or board[i][j - 1] != '-':
                    count += 1
            elif board[i][j] == '|':
                if i == 0 or board[i - 1][j] != '|':
                    count += 1
    return count

n, m = map(int, input().split())
board = [input() for _ in range(n)]
    
print(solution(n, m, board))