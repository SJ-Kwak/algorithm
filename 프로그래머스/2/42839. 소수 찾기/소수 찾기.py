import itertools

def solution(numbers):
    answer = 0
    nums = []
    for i in range(1, len(numbers)+1):
        nPr = list(itertools.permutations(numbers, i))
        for j in range(len(nPr)):
            nums.append(int(''.join(nPr[j])))
    nums = set(nums)
    for n in nums:
        check = True
        for i in range(2, n):
            if n % i == 0:
                check = False
                break
        if check and n not in [0,1]:
            answer += 1
    return answer