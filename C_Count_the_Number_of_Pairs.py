t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    lower = [0] * 26
    upper = [0] * 26
    
    for c in s:
        if c.islower():
            lower[ord(c) - ord('a')] += 1
        else:
            upper[ord(c) - ord('A')] += 1
    
    pairs = 0
    extra = 0
    for j in range(26):
        pairs += min(lower[j], upper[j])
        extra += abs(lower[j] - upper[j]) // 2

    add = min(extra, k)
    
    print(pairs + add)
