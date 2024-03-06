p = input()
stack = []
l = 0
for i in range(len(p)):
    if p[i] == '(':
        stack.append(p)
    else:
        if p[i-1] == '(':
            stack.pop()
            l += len(stack)
        else:
            stack.pop()
            l += 1
print(l)