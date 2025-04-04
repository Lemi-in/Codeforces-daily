N = 0
L = 0
R = 0
C = [0] * 200001
lcnt = [0] * 200001
rcnt = [0] * 200001

T = int(input())
while T > 0:
    T -= 1
    N, L, R = map(int, input().split())
    
    for i in range(1, N + 1):
        lcnt[i] = 0
        rcnt[i] = 0
    C = list(map(int, input().split()))
    for i in range(1, N + 1):
        if i <= L:
            lcnt[C[i]] += 1
        else:
            rcnt[C[i]] += 1

    for i in range(1, N + 1):
        mn = min(lcnt[i], rcnt[i])
        lcnt[i] -= mn
        rcnt[i] -= mn
        L -= mn
        R -= mn

    if L < R:
        lcnt, rcnt = rcnt, lcnt
        L, R = R, L

    ans = 0
    for i in range(1, N + 1):
        extra = L - R
        canDo = lcnt[i] // 2
        Do = min(canDo * 2, extra)
        ans += Do // 2
        L -= Do

    ans += (L - R) // 2 + (L + R) // 2
    print(ans)
