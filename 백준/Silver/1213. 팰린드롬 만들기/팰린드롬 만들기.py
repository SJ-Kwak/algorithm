from collections import Counter

s = str(input())
c = sorted(Counter(s).items())

odd = 0
for k, v in c:
    if v % 2 != 0:
        odd += 1

if odd > 1:
    print("I'm Sorry Hansoo")
    exit()

answer = ''
m = ''
for k, v in c:
    if v % 2 != 0:
        m = k
    answer += k * (v//2)
        
answer = answer + m + answer[::-1]
print(answer)