# 4-1 상하좌우
n = int(input())
a = list(map(str, input().split()))

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dir = ['L', 'R', 'U', 'D']

x, y = 1, 1

for i in a:
    # 이동 좌표 설정
    for j in range(4):
        if i == dir[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    # 공간 벗어나면 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)