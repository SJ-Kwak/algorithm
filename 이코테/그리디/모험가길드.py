# 모험가 길드
n = int(input())
x = list(map(int, input().split()))
x.sort()

group = 0
person = 0

for i in x:     # 오름차순 정렬된 리스트
    person += 1 # 현재 그룹에 해당 모험가 포함
    if person >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        group += 1  
        person = 0
    
print(group)
