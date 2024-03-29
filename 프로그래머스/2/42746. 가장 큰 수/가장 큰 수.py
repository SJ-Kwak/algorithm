def solution(numbers):
    numbers = list(map(str, numbers))
    # 문자열 3번 반복시켜서 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))