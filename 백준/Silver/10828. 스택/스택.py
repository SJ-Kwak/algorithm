import sys

n = int(input())

stack = []

for i in range(n):
    cmd = sys.stdin.readline().split()
    x = 0
    if(len(cmd) > 1):
        x = cmd[1]
    cmd = cmd[0]
    
    if cmd=='push':
        stack.append(x)
    elif cmd=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif cmd=='size':
        print(len(stack))
    elif cmd=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif cmd=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])