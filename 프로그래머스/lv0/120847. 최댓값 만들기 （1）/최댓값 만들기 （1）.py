def solution(numbers):
    m1=numbers.pop(numbers.index(max(numbers)))
    m2=numbers.pop(numbers.index(max(numbers)))
    answer=m1*m2
    return answer