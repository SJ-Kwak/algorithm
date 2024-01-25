from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    index = deque(i for i in range(len(priorities)))
    while queue:
        cur = queue.popleft()
        idx = index.popleft()
        if any(cur < p for p in queue):
            queue.append(cur)
            index.append(idx)
        else:
            answer += 1
            if idx == location:
                break
    return answer