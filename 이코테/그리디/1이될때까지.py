# 3-4 1이 될 때까지
n, k = map(int, input().split())
count = 0
while True:
    if n == 1:
        break
    else:
        if n % k == 0:
            n = n/k
        else:
            n -= 1
        count += 1

print(count)

# 해설: O(log n)
result = 0
while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을 때 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

# 남은 수에 대하여 1씩 빼기
result += (n - 1)