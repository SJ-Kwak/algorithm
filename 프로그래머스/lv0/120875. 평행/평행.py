def solution(dots):
    answer = 0
    if inclination(dots[0], dots[1]) == inclination(dots[2], dots[3]):
        answer = 1
    elif inclination(dots[0], dots[2]) == inclination(dots[1], dots[3]):
        answer = 1
    elif inclination(dots[0], dots[3]) == inclination(dots[1], dots[2]):
        answer = 1
    
    return answer

def inclination(a, b):
    return (b[1]-a[1]) / (b[0]-a[0])