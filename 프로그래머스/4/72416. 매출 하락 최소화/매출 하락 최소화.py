def tree(links):
    tree = [[] for _ in range(len(links) + 2)]
    for x, y in links:
        tree[x].append(y)
    return tree

def dfs(sales, v, dp, tree):
    dp[v][0] = 0
    dp[v][1] = sales[v-1] # 직원번호, 참석 = 매출액
    money = 0
    
    for k in tree[v]:
        dfs(sales, k, dp, tree)
        money += min(dp[k][0], dp[k][1])
        
    dp[v][1] = money + sales[v-1]  # 자신이 참석
    # 자신이 참석 X
    if any(dp[k][0] > dp[k][1] for k in tree[v]):
        dp[v][0] = money
    else:
        dp[v][0] = money + min((dp[k][1] - dp[k][0] for k in tree[v]), default=0)

def solution(sales, links):
    dp = [[0,0] for _ in range(len(sales) + 1)]
    tree_struct = tree(links)
    dfs(sales, 1, dp, tree_struct)
    
    return min(dp[1][0], dp[1][1])