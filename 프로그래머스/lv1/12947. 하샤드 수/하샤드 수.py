def solution(x):
    arr = list(map(int, str(x)))
    return True if x%sum(arr)==0 else False