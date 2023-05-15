import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
result = 0
tmp = 0
for i in arr:
    tmp += i
    result += tmp
print(result)