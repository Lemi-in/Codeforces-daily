t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    fountains = set()
    for _ in range(k):
        r, c = map(int, input().split())
        fountains.add((r, c))
    
    alpha = n + m - 2
    ans = []
    for r, c in fountains:
        if r == n or c == 1:
            ans.append(0)
        else:
            ans.append(1)
    
    print(alpha)
    print(' '.join(map(str, ans)))