from collections import deque

n, days = map(int, input().split())
arr = list(map(int, input().split()))
q = deque()
mx = 0
idx = []
l, r = 0, 0

while r < n:
    q.append((arr[r], r))
    while sum(x[0] for x in q) > days:
        l += 1
        q.popleft()
    if len(q) > mx:
        mx = len(q)
        idx = sorted([x[1] + 1 for x in q])
    r += 1

print(mx)
print(*idx)