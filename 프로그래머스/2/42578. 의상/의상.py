from collections import Counter

def solution(clothes):
    answer = 1
    clothes_dict = Counter(ct for n, ct in clothes)
    
    for c in clothes_dict.values():
        answer *= (c + 1)
    
    return answer - 1