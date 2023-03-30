n = int(input())
s = ','.join(str(input()))
l = list(map(int, s.split(',')))
print(sum(l))