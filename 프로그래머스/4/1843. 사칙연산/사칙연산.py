from functools import lru_cache

def solution(arr):

    @lru_cache(None)
    def dfs(start, end):
        if start == end:
            val = int(arr[start])
            return val, val

        min_val = float('inf')
        max_val = float('-inf')

        for i in range(start + 1, end, 2):
            op = arr[i]

            left_min, left_max = dfs(start, i - 1)
            right_min, right_max = dfs(i + 1, end)

            if op == '+':
                min_val = min(min_val, left_min + right_min)
                max_val = max(max_val, left_max + right_max)
            elif op == '-':
                min_val = min(min_val, left_min - right_max)
                max_val = max(max_val, left_max - right_min)

        return min_val, max_val

    _, result = dfs(0, len(arr) - 1)
    return result