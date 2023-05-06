# 6-10 위에서 아래로
n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)

for i in arr:
    print(i, end=' ')