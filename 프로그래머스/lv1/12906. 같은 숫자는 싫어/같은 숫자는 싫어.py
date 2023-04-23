def solution(arr):
    answer = []
    tmp = None
    for i in arr:
        if i != tmp:
            answer.append(i)
            tmp = i
    return answer