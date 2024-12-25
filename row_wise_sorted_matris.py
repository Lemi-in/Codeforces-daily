from collections import defaultdict

matrix = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
n = len(matrix)
mp = defaultdict(int)
cnt = 0
for mat in matrix:
    cnt += 1
    for i in range(len(mat)):
        if mp[mat[i]] <= cnt:
            mp[mat[i]] += 1

print(mp)
small = -1
for key, val in mp.items():
    if val == n:
        small = key
        break
print(small)



