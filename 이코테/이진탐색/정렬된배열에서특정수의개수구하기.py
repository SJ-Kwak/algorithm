from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
num = list(map(int, input().split()))

def count_by_range(a, left, right):
    right_idx = bisect_right(a, right)
    left_idx = bisect_left(a, left)
    return right_idx - left_idx

count = count_by_range(num, x, x)

if count == 0:
    print(-1)
else:
    print(count)