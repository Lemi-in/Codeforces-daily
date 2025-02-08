def ls(): return input().split()
def ints(): return map(int, input().split())
def strs():return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

mat = []
for i in range(5):
    a = li()
    mat.append(a)
cnt = 0
for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            idx = (i ,j)

print(abs(idx[0] - 2 ) + abs(idx[1] - 2))
