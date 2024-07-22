t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pref_max = 0
    s = 0
    mx = 0

    for i in range(n):
        pref_max = max(pref_max, a[i])
        
        d = pref_max - a[i]
        s += d
        mx = max(mx, d)

    print(s + mx)
