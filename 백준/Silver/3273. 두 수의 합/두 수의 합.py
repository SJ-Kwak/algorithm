n = int(input())
data = list(map(int, input().split()))
data.sort()
x = int(input())

tmp = 0
count = 0
start, end = 0, n-1

while start < end:
    tmp = data[start] + data[end]
    if tmp == x:
        count += 1
    if tmp < x:
        start += 1
        continue
    end -= 1

print(count)