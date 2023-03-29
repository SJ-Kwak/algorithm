import sys
l = list(map(int, (sys.stdin.readline() for _ in range(10))))
k = list(n%42 for n in l)
s = set(k)
print(len(s))