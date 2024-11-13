import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

def solution(n, k, coins):
    answer = 0
    coins.sort(reverse=True)
    num = 0
    for coin in coins:
        if coin > k:
            continue
        else:
            answer += k // coin
            k %= coin
            if k == 0:
                break
    return answer

print(solution(n, k, coins))