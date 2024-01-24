def solution(money):
    answer = 0
    # 첫집 선택. 마지막집 제외.
    first = [0] * len(money)
    first[0] = money[0]
    first[1] = max(money[0], money[1])
    for i in range(2, len(money)-1):
        first[i] = max(first[i-1], first[i-2]+money[i])
    
    # 마지막집 선택. 첫집 제외.
    last = [0] * len(money)
    last[0] = 0
    last[1] = money[1]
    for i in range(2, len(money)):
        last[i] = max(last[i-1], last[i-2]+money[i])
    
    answer = max(max(first), max(last))
    return answer