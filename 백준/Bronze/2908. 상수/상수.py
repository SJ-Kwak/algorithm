a,b = map(str, input().split())
l = [int(a[::-1]), int(b[::-1])]
print(max(l))