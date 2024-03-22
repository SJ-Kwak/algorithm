from collections import deque

n = int(input())
k = int(input())
apple = [tuple(map(int, input().split())) for _ in range(k)]
l = int(input())
snake_dir = [input().split() for _ in range(l)]

snake = deque([(1, 1)])
direction = 0
time = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

apple_set = set(apple)

while True:
    time += 1
    
    nx = snake[0][0] + dx[direction]
    ny = snake[0][1] + dy[direction]
    
    if (nx < 1 or nx > n or ny < 1 or ny > n) or ((nx, ny) in snake and len(snake) > 1):
        break
    
    snake.appendleft((nx, ny))
    
    if (nx, ny) in apple_set:
        apple_set.remove((nx, ny))
    else:
        snake.pop()
        
    if snake_dir and time == int(snake_dir[0][0]):
        if snake_dir[0][1] == 'D':  # 시계 방향 90도
            direction = (direction + 1) % 4
        else:   # 반시계 방향 90도
            direction = (direction - 1) % 4
        snake_dir.pop(0)

print(time)