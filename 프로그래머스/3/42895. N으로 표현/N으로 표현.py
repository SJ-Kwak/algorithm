def solution(N, number):
    arr = [[] for _ in range(9)]
    
    for i in range(1,9):
        # 사칙연산 없이 N, NN, NNN, ...
        arr[i].append(int(str(N) * i))
        
        for j in range(1,i):
            for x in arr[j]:    # N을 j번 사용
                for y in arr[i-j]:  # N을 i-j번 사용
                    arr[i].append(x+y)
                    arr[i].append(x-y)
                    arr[i].append(x*y)
                    if y != 0:
                        arr[i].append(x//y)
                        
        if number in arr[i]:
            return i
    
    return -1