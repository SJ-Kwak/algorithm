def solution(brown, yellow):
    answer = []
    width, height = 0, 0
    for w in range(2, brown+yellow):
        for h in range(2, w + 1):
            if w * h == (brown+yellow) and w >= h and (w-2) * (h-2) == yellow:
                return [w, h]