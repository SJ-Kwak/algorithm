import sys
sys.setrecursionlimit(10**6)

pre = []
while True:
    try:
        n = int(sys.stdin.readline().rstrip())
        pre.append(n)
    except:
        break

def post_order(s, e):
    if s>e:
        return
    root = e+1
    for i in range(s+1, e+1):
        if pre[s] < pre[i]:
            root = i
            break
    post_order(s+1, root-1)
    post_order(root, e)
    print(pre[s])

post_order(0, len(pre)-1)