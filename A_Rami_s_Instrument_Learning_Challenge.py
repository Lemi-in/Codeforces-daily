import heapq

n, k = map(int, input().split())
days = list(map(int, input().split()))

pq = [(day, i) for i, day in enumerate(days, 1)]
heapq.heapify(pq)

m = 0
learned = []
while pq and k >= pq[0][0]:
    day, i = heapq.heappop(pq)
    k -= day
    m += 1
    learned.append(i)

print(m)
print(*learned)