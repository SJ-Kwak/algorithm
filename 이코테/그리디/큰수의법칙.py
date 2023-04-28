# 3-2 큰 수의 법칙
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse = True)
first = arr[0]
second = arr[1]
result = 0

while True:
    if m == 0:
        break
    for i in range(k):
        result += first
        m -= 1
    result += second
    m -= 1

print(result)

# 해설
# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first   # 가장 큰 수 더하기
result += (m - count) * second  # 두번째 수 더하기