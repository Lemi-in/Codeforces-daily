def f(m):
    if m == 0:
        return 0
    if m == 1:
        return 0
    mm = m - 1
    p = 31 - mm.bit_length()
    if m == (1 << p):
        return (1 << p) - 1
    else:
        return (1 << (p + 1)) - 1

def solve():
    n, x = map(int, input().split())

    best_m = 0
    for m in range(n + 1):
        if m == 0:
            best_m = 0
        else:
            base = f(m)
            if (base & (~x)) != 0:
                continue

            needed = m if base == x else m + 1

            if needed <= n:
                best_m = m

    distinct = []
    if best_m == 0:
        distinct.append(x)
    else:
        for i in range(best_m):
            distinct.append(i)
        base = f(best_m)
        if base != x:
            extra = x & (~base)
            distinct.append(extra)

    ans = list(distinct)

    filler = 0 if best_m > 0 else x
    while len(ans) < n:
        ans.append(filler)

    print(*ans)

t = int(input())
for _ in range(t):
    solve()