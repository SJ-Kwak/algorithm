def solution(n):
    mod = 1000000007
    if n % 2 != 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3
    for i in range(4, n + 1, 2):
        dp[i] = 3 * dp[i-2]
        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2
        dp[i] %= mod
    return dp[n]