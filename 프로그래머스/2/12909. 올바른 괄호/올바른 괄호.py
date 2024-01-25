def solution(s):
    data = []
    for p in s:
        if p == '(':
            data.append(p)
        else:
            if not data:
                return False
            data.pop()
    return not data