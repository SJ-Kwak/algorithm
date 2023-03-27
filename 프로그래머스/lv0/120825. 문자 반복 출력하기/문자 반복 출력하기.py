def solution(my_string, n):
    answer = list(n*i for i in my_string)
    return ''.join(answer)