import sys
l = list(map(int, (sys.stdin.readline() for _ in range(28))))
answer = []
for i in range(1,31):
    if(l.count(i)!=1):
        answer.append(i)
print(answer.pop(answer.index(min(answer))))
print(answer.pop())