n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
result = float('inf')

def TPS(start, end, visited, cost):
    global result
    if end == n and graph[start][0] != 0:
        result = min(result, cost + graph[start][0])
        return
        
    for i in range(1, n):
        if not visited[i] and graph[start][i] != 0:
            visited[i] = True
            TPS(i, end + 1, visited, cost + graph[start][i])
            visited[i] = False
        
TPS(0, 1, visited, 0)
print(result)