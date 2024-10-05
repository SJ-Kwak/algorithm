n, k = map(int, input().split())
nums = list(map(int, input().split()))

arr = sorted(nums, key=lambda x: (bin(x).count('1'), x), reverse=True)
print(arr[k-1])