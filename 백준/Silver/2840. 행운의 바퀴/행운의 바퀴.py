import sys
input = sys.stdin.readline

n, k = map(int, input().split())
wheel = ['?'] * n
check = True
idx = 0

for _ in range(k):
    num, alp = input().split()
    idx = (idx + int(num)) % n
    if wheel[idx] == '?':
        wheel[idx] = alp
    elif wheel[idx] == alp:
        continue
    else:
        check = False
        break

for i in range(n-1):
    if wheel[i] == '?':
        continue
    for j in range(i+1, n):
        if wheel[i] == wheel[j]:
            check = False
            break

if not check:
    print('!')
else:
    for i in range(n):
        print(wheel[idx], end='')
        idx -= 1
