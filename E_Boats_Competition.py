t = int(input())
for _ in range(t):
    n = int(input())
    weights = list(map(int, input().split()))
    occu = {}
    maxx = 0
    for w in weights:
        occu[w] = occu.get(w, 0) + 1
    s = 2
    while s <= 2 * n:
        teams = 0
        for w in occu:
            if s - w in occu:
                teams += min(occu[w], occu[s - w])
        maxx = max(maxx, teams // 2)
        s += 1
    
    print(maxx)
