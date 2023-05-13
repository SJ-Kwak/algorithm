# 7-8 떡볶이 떡 만들기
n, m = map(int, input().split())
height = list(map(int, input().split()))

start = 0
end = max(height)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for h in height:
        if h > mid:
            total += h - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    
print(result)