def solution(name):
    answer = 0
    length = len(name)
    # 위치 변경 비용
    move = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]
    answer += sum(move)
    
    # 커서 이동 비용
    min_move = length - 1
    
    for i in range(length):
        tmp = i + 1
        while tmp < length and name[tmp] == 'A':
            tmp += 1
        move = i + (length - tmp) + min(i, length - tmp)
        min_move = min(min_move, move)
        
    answer += min_move
    
    return answer