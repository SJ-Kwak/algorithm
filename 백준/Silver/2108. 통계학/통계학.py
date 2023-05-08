import sys
from collections import Counter

n = int(input())
arr = list(int(sys.stdin.readline().rstrip()) for _ in range(n))
arr.sort()
def solution(array):
    count = Counter(array)
    m = max(count.values())
    modes = [k for k, v in count.items() if v == m]
    return sorted(modes)[1] if len(modes) > 1 else modes[0]
print(round(sum(arr)/n))
print(arr[n//2])
print(solution(arr))
print(max(arr)-min(arr))