def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n
    while start <= end:
        ppl = 0
        mid = (start + end) // 2
        
        for t in times:
            ppl += mid // t
            
            if ppl >= n:
                break
            
        if ppl >= n:
            answer = mid
            end = mid-1
        else:
            start = mid+1
        
    return answer
            
        
        
    
    
    