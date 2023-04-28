# 3-1 거스름돈
n = 1260
list = [500, 100, 50, 10]
coin = 0
for i in list:      # O(n). n: 동전 종류
    coin += n // i
    n %= i
print(coin)