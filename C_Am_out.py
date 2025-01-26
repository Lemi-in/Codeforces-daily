t = int(input())
res = []

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    stack = []
    cost = 0

    for i in range(n):
        if s[i] == '(' or (s[i] == '_' and len(stack) == 0):
            stack.append(i + 1)
        else:
            cost += i + 1 - stack.pop()

    res.append(cost)

for r in res:
    print(r)
