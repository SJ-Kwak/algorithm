import heapq

def solution(operations):
    maxq = []
    minq = []
    for op in operations:
        cmd, n = op.split()
        n = int(n)
        if cmd == 'I':
            heapq.heappush(maxq, n)
            heapq.heappush(minq, -n)
        else:
            if not maxq:
                continue
            if n > 0:
                pop = heapq.heappop(minq)
                maxq.remove(-pop)
            else:
                pop = heapq.heappop(maxq)
                minq.remove(-pop)

    if maxq:
        return [max(maxq), min(maxq)]
    else:
        return [0, 0]