n = 1000 - int(input())
count = 0
coin = [500, 100, 50, 10, 5, 1]
i = 0
while n != 0:
    count += n // coin[i]
    n %= coin[i]
    i += 1
print(count)