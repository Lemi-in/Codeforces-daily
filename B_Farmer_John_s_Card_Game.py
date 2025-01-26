def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

for _ in range(it()):
    mat = []
    ans = []
    n, m = ints()
    for idx in range(1, n + 1):
        a = li()
        a.sort()
        mat.append([a, idx])
    mat.sort()  
    for i in range(m):
        for j in range(n):
            if i < len(mat[j][0]):
                ans.append(mat[j][0][i])
    possible = True
    for i in range(1, len(ans)):
        if ans[i] < ans[i - 1]:
            possible = False
            break
    if not possible:
        print(-1)

    else:
        res = []
        for x , y in mat:
            res.append(y)
        print(*res)

