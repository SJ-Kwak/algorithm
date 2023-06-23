import sys

n = int(input())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

start, end = 0, n-1
x = abs(data[start] + data[end])
answer = [data[start], data[end]]

while start < end:
    tmp = data[start] + data[end]
    if abs(tmp) < x:
        x = abs(tmp)
        answer = [data[start], data[end]]
        if x == 0:
            break
    if tmp < 0:
        start += 1
    else:
        end -= 1


print(answer[0], answer[1])