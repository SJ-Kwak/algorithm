def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, wires):
    answer = 0
    parent = [i for i in range(n + 1)]

    diff = float('inf')

    for wire in wires:
        u, v = wire
        parent = [i for i in range(n + 1)]
        
        for other_wire in wires:
            if other_wire != wire:
                union_find(parent, other_wire[0], other_wire[1])

        count = [0] * (n + 1)
        for i in range(1, n + 1):
            root = find_parent(parent, i)
            count[root] += 1
        
        sizes = [c for c in count if c > 0]
        if len(sizes) == 2:
            diff = min(diff, abs(sizes[0] - sizes[1]))

    return diff