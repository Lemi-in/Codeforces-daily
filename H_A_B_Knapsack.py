def main():
    n, m, s, a, b = map(int, input().split())
    va = list(map(int, input().split()))
    vb = list(map(int, input().split()))

    va.sort(reverse=True)
    vb.sort(reverse=True)
    
    r = min(n, s // a) - 1
    total_sum = (r + 1) * a
    ans = sum(va[:r + 1])
    cur = ans

    for l in range(min(m, s // b)):
        cur += vb[l]
        total_sum += b
        while total_sum > s:
            total_sum -= a
            cur -= va[r]
            r -= 1
        ans = max(ans, cur)
    
    print(ans)

if __name__ == "__main__":
    main()
