from collections import deque

def solution(n, computers):
    answer = 0
    q = deque([])
    visited = [False] * n
    
    def bfs(start):
        nonlocal answer
        q = deque([start])
        while q:
            node = q.popleft()
            if not visited[node]:
                visited[node] = True
                for i in range(n):
                    if not visited[i] and computers[node][i] == 1:
                        q.append(i)
        answer += 1
        
    for i in range(n):
        if not visited[i]:
            bfs(i)

    return answer