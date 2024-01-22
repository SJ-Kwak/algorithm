from collections import deque

def solution(n, edge):
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    answer = bfs(graph, 1, visited, distance)
    return answer.count(max(answer))

def bfs(graph, start, visited, distance):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1
                
    return distance