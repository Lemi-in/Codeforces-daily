n = int(input())
p = [int(input()) for _ in range(n)]

mxDep = 0

for i in range(n):
    dep = 0
    curr = i
    while p[curr] != -1:
        curr = p[curr] - 1
        dep += 1
    
    mxDep = max(mxDep, dep + 1)

print(mxDep)
