# 3-3 숫자 카드 게임
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
_min = []
for i in arr:
    _min.append(min(i))
print(max(_min))