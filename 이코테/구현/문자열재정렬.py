# 문자열 재정렬
arr = input()
alp, num = [], 0

for a in arr:
    if a.isalpha():
        alp.append(a)
    else:
        num += int(a)

alp.sort()

print(''.join(alp)+str(num))