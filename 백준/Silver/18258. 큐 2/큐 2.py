import sys
from collections import deque

n = int(input())

queue = deque()

for i in range(n):
    cmd = sys.stdin.readline().split()
    x = 0
    if(len(cmd) > 1):
        x = cmd[1]
    cmd = cmd[0]
    
    if cmd=='push':
        queue.append(x)
    elif cmd=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd=='size':
        print(len(queue))
    elif cmd=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif cmd=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif cmd=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])