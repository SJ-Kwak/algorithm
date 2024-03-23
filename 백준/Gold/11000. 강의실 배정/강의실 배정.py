import heapq
import sys

def solution(lectures):
    room = []
    lectures.sort()
    heapq.heappush(room, lectures[0][1])
    
    for i in range(1, n):
        if lectures[i][0] < room[0]:
            heapq.heappush(room, lectures[i][1])
        else:
            heapq.heappop(room)
            heapq.heappush(room, lectures[i][1])
            
    return len(room)

n = int(input())
q = []

for _ in range(n):
    s, t = map(int, sys.stdin.readline().split())
    q.append([s,t])
print(solution(q))