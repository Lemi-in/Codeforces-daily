n = int(input())
array = list(map(int, input().split()))
array.sort()
mex = 1
for num in array:
    if num >= mex:
        mex += 1
print(mex)
