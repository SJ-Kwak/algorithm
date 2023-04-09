def solution(num, total):
    answer = []
    avg = total // num
    var = 1
    if num % 2 == 0: 
        num -= 1
        var = 2
    answer = [i for i in range(avg-num//2, avg+num//2+var)]
    return answer