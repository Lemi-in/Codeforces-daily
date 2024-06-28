n = int(input())
a = list(map(int, input().split()))
a.sort()
mex = 1
for ai in a:
    if ai >= mex:
        mex += 1
print(mex)
