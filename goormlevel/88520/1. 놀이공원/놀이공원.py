t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	land = list(list(map(int, input().split())) for _ in range(n))
	
	dp = [[0] * (n+1) for _ in range(n+1)]
	
	for i in range(1, n+1):
		for j in range(1, n+1):
			dp[i][j] = land[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
	
	result = float('inf')

	for a in range(n-k+1):
		for b in range(n-k+1):
			answer = dp[a+k][b+k] - dp[a][b+k] - dp[a+k][b] + dp[a][b]
			result = min(result, answer)

	print(result)