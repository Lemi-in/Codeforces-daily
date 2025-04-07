t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a_sorted = sorted(a)
    ok = True

    for i in range(0, 2 * n, 2):

        left_diff = abs(a_sorted[i] - a_sorted[i+1])

        if i > 0:
            if abs(a_sorted[i] - a_sorted[i-1]) < left_diff:
                ok = False
                break
        if i+2 < 2 * n:
            if abs(a_sorted[i+1] - a_sorted[i+2]) < left_diff:
                ok = False
                break

    print("YES" if ok else "NO")
