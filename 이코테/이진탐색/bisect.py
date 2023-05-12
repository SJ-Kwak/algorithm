# 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

'''
bisect_left(a, x): 정렬된 순서 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
bisect_right(a, x): 정렬된 순서 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환
'''

# 값이 [left, right]인 데이터 개수 반환
def count_by_range(a, left, right):
    right_idx = bisect_right(a, right)
    left_idx = bisect_left(a, left)
    return right_idx - left_idx

a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))