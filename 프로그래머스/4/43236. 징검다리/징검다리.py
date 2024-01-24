def solution(distance, rocks, n):
    answer = 0
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    
    dist = []
    for i in range(1, len(rocks)):
        dist.append(rocks[i] - rocks[i-1])
    
    start, end = 0, distance
    while start <= end:
        mid = (start + end) // 2
        removed, cur = 0,0
        
        for d in dist:
            cur += d
            if cur < mid:
                removed += 1
            else:
                cur = 0
        
        if removed > n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    return answer