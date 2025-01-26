def solve():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))

    ans = 0
    j = 0  

    for r in range(n):
        # Move `j` to the first index where `v[j] > v[r] + k`
        while j < n and v[j] <= v[r] + k:
            j += 1
        ans += n - j  # Add all indices greater than `j` to the count hioj gug y8g yg y8 gyf y8 y  tuy yugt tuy tyt tfd tyr u hf ryt y  0uhfrdf ftrf uyt t

    print(ans)

solve()
