def solution(n):
    answer = sorted(list(map(int, str(n))))
    answer.reverse()
    result = ''.join(map(str, answer))
    return int(result)