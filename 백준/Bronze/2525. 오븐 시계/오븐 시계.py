a, b = map(int, input().split())
c = int(input())

a += (b+c)//60
b = (b+c)%60

if(b>59):
    a+=1
    b-=60

if(a>23):
    a-=24

print(a, b)