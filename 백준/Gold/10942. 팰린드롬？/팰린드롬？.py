import sys
input = sys.stdin.readline

def solution(n, nums, question):
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
    
    for i in range(n-1):
        if nums[i] == nums[i+1]:
            dp[i][i+1] = 1
    
    for i in range(2, n): 
        for j in range(n-i):
            if nums[j] == nums[j+i] and dp[j+1][j+i-1]:
                dp[j][j+i] = 1
    
    results = []
    for s, e in question:
        results.append(dp[s-1][e-1])
    
    return results
    
n = int(input())
nums = [n for n in map(int, input().split())]
m = int(input())
question = [list(map(int, input().split())) for _ in range(m)]

results = solution(n, nums, question)
print("\n".join(map(str, results)))