import sys
n = int(input())
l = list(map(int, sys.stdin.readline().split()))
m = max(l)
r = []
for i in l:
    r.append(i/m*100)
print(sum(r)/n)