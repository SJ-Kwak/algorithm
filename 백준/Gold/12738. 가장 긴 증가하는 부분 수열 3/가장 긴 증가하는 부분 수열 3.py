n = int(input())
arr = list(map(int, input().split()))

def binary_search(start, end, target):
    if start > end:
        return start
        
    mid = (start + end) // 2
    
    if result[mid] > target:
        return binary_search(start, mid-1, target)
    elif result[mid] < target:
        return binary_search(mid+1, end, target)
    else:
        return mid

result = [arr[0]]
for i in range(1, len(arr)):
    if arr[i] > result[-1]:
        result.append(arr[i])
    else:
        result[binary_search(0, len(result)-1, arr[i])] = arr[i]

print(len(result))