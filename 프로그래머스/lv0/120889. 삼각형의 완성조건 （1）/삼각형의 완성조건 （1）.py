def solution(sides):
    answer = 0
    long = sides.pop(sides.index(max(sides)))
    if sum(sides)>long:
        answer=1
    else:
        answer=2
    return answer