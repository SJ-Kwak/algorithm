import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2 and scoville[0] < K:  # heap은 최솟값이 0번째
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2 * b)
        
    if scoville[0] < K:
        return -1
    return answer