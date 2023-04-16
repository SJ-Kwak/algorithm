def solution(a, b):
    arr = []
    t = 0
    if a > b:
        t = a
        a = b
        b = t
    for i in range(a, b+1):
        arr.append(i)
    return sum(arr)