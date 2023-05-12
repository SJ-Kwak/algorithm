# 재귀함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간값 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간값보다 target값이 작은 경우: 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

# 반복문
def __binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간값 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간값보다 target값이 작은 경우: 왼쪽 확인
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
        return None
        
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result+1)

__result = __binary_search(array, target, 0, n-1)
if __result == None:
    print('원소가 존재하지 않습니다')
else:
    print(__result+1)