import sys
t = int(input())
for i in range(0,t):
    a,b=map(int,sys.stdin.readline().split())
    print('Case #%d:'%(i+1),'%d + %d ='%(a,b),a+b)