from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = defaultdict(int)

    b = []
    for i in range(n):
        freq[a[i]] += 1
        mx = max(freq, key=freq.get)
        b.append(mx)
    print(*b)
            
