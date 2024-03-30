from collections import deque

def is_diff(w1, w2):
    cnt = 0
    for x, y in zip(w1, w2):
        if x != y:
            cnt += 1
        if cnt > 1:
            return False
    return True   

def solution(begin, target, words):
    if target not in words:
        return 0
    q = deque([(begin, 0)])
    visited = [False] * len(words)
    while q:
        cur, answer = q.popleft()
        if target == cur:
            return answer
        for i, word in enumerate(words):
            if not visited[i] and is_diff(word, cur):
                visited[i] = True
                q.append((word, answer + 1))