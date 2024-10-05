from itertools import product

def solution(word):
    answer = 0
    alphabets = ['A', 'E', 'I', 'O', 'U']
    
    dicts = []
    for r in range(1, 6):
        dicts += product(alphabets, repeat = r)
        
    words = [''.join(map(str, t)) for t in dicts]
    words.sort()
    
    for i in range(len(words)):
        if words[i] == word:
            answer = i + 1
            break
    
    return answer