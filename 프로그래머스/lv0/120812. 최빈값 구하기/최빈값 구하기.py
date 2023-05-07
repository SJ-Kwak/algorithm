def solution(array):
    count = {}
    for i in array:
        count[i] = array.count(i)
    k = list(count.keys())
    l = list(count.values())
    m = max(l)
    i = l.index(m)
    if l.count(m) > 1:
        return -1
    return k[i]