# 6-11 성적이 낮은 순서대로 학생 출력하기
n = int(input())
arr = list(list(map(str, input().split())) for _ in range(n))

arr = sorted(arr, key=lambda std:std[1])

for i in arr:
    print(i[0], end=' ')