import sys
n = int(input())
d = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            d[i][j] += d[i-1][0]
        elif j == i:
            d[i][j] += d[i-1][-1]
        else:
            d[i][j] += max(d[i-1][j-1], d[i-1][j])

print(max(d[-1]))