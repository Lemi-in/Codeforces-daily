# t = int(input())
# for _ in range(t):
#     n = int(input())
#     lamps = [[] for _ in range(n+1)]
#     for _ in range(n):
#         a, b = map(int, input().split())
#         lamps[a].append(b)
#     print(lamps)
#     score = 0
#     for i in range(1, n+1):
#         lamps[i].sort(reverse=True)
#         score += sum(lamps[i][:min(i, len(lamps[i]))])
#     print(score)
t = int(input())
for _ in range(t):
    n = int(input())
    lamps = []
    for _ in range(n):
        a, b = map(int, input().split())
        lamps.append((a, b))
    lamps.sort(key=lambda x: (x[0], -x[1]))
    score = 0
    cnt = [0] * (n + 1)
    for a, b in lamps:
        if cnt[a] < a:
            score += b
            cnt[a] += 1
    print(score)