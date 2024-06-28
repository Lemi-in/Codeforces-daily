from bisect import bisect_right

n = int(input())
x = list(map(int, input().split()))
q = int(input())
x.sort()

for _ in range(q):
    m = int(input())
    cnt = bisect_right(x, m)
    print(cnt)
