def solution(n, lost, reserve):
    answer = 0
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    found = 0
    for num in lost_set:
        if num-1 in reserve_set:
            found += 1
            reserve_set.remove(num-1)
        elif num+1 in reserve_set:
            found += 1
            reserve_set.remove(num+1)

    answer = n - (len(lost_set)-found)
    return answer