# 4-3 왕실의 나이트
pos = input()
x = ord(pos[0])-96   # ord(): 알파벳 -> 정수 변환. a: 97
y = int(pos[1])

dx = [2, 2, 1, -1, -2, -2, 1, -1]
dy = [1, -1, 2, 2, 1, -1, -2, -2]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)

# 해설
# 나이트가 이동할 수 있는 8가지 방향을 하나의 배열에 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (2, -1), (-1, 2), (-2, 1)]
result = 0

for step in steps:
    # 이동할 위치 확인
    next_row = x + step[0]
    next_col = y + step[1]

    # 이동 가능할 경우
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1