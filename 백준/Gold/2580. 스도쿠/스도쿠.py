import sys

def check(box, row, col, num):
    for i in range(9):
        if box[row][i] == num or box[i][col] == num:
            return False
            
    # 3 * 3 
    srow, scol = 3 * (row // 3), 3 * (col // 3)
    for i in range(srow, srow + 3):
        for j in range(scol, scol + 3):
            if box[i][j] == num:
                return False
                
    return True
    
def solve(box):
    for i in range(9):
        for j in range(9):
            if box[i][j] == 0:
                for num in range(1,10):
                    if check(box, i, j, num):
                        box[i][j] = num
                        if solve(box):
                            return True
                        box[i][j] = 0 # 백트래킹
                return False
    return True
    
def solution(sudoku):
    answer = [[0] * 9 for _ in range(9)]
    solve(sudoku)
    return sudoku
    
sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
for row in solution(sudoku):
    print(*row)