def solve():
    n1 = int(input())
    caps = sorted(map(int, input().split()))
    n2 = int(input())
    shirts = sorted(map(int, input().split()))
    n3 = int(input())
    pants = sorted(map(int, input().split()))
    n4 = int(input())
    shoes = sorted(map(int, input().split()))

    i, j, k, l = 0, 0, 0, 0
    min_diff = float('inf')
    result = (0, 0, 0, 0)

    while i < n1 and j < n2 and k < n3 and l < n4:
        a, b, c, d = caps[i], shirts[j], pants[k], shoes[l]
        current_max = max(a, b, c, d)
        current_min = min(a, b, c, d)
        current_diff = current_max - current_min

        if current_diff < min_diff:
            min_diff = current_diff
            result = (a, b, c, d)

        if current_min == a:
            i += 1
        elif current_min == b:
            j += 1
        elif current_min == c:
            k += 1
        else:
            l += 1

    print(*result)

solve()
