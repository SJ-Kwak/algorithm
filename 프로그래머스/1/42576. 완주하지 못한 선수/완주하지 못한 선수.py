from collections import Counter

def solution(participant, completion):
    answer = ''
    p = Counter(participant)
    c = Counter(completion)
    
    p.subtract(c)
    for k, v in p.items():
        if v > 0:
            answer = k
    return answer