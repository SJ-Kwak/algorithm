def solution(n):
    answer = 0
    x = n**(1/2)
    answer = (x+1)**2 if x == int(x) else -1
    return answer