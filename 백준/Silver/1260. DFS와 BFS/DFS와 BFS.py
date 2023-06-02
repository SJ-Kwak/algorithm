import sys
from collections import deque
n, m, v = map(int, input().split())

g = [[False] * (n+1) for _ in range(n+1)]
marker1 = [False] * (n+1)
marker2 = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    g[a][b] = True
    g[b][a] = True

def dfs(g, v, m):
    print(v, end=' ')
    m[v] = True
    for i in range(1, n+1):
        if g[v][i] and not m[i]:
            dfs(g, i, m)

def bfs(g, v, m):
    q = deque()
    q.append(v)
    m[v] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if g[v][i] and not m[i]:
                q.append(i)
                m[i] = True

dfs(g, v, marker1)
print()
bfs(g, v, marker2)