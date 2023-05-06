arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(arr)):
    minIdx = i
    for j in range(i+1, len(arr)):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]   # Swap

print(arr)