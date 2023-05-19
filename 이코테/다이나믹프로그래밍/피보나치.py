# 단순 재귀
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

# Top Down DP
d = [0] * 100   # 한 번 계산된 결과를 memoization하기 위한 리스트 초기화
def fibo_top(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:   # 이미 계산한 적 있는 문제라면 그대로 반환
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 결과 반환
    d[x] = fibo_top(x-1) + fibo_top(x-2)
    return d[x]

# Bottom Up DP
d = [0] * 100
d[1], d[2] = 1, 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

