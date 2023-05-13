# 7-5 부품 찾기
n = int(input())
remain = list(map(int, input().split()))
m = int(input())
sales = list(map(int, input().split()))
remain.sort()

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
    
for s in sales:
    result = __binary_search(remain, s, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')