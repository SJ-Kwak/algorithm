import sys
n = int(input())
arr = list(int(sys.stdin.readline().rstrip()) for _ in range(n))
arr.sort()
for i in arr:
    print(i)