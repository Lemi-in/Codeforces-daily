import itertools

t = int(input())
while t > 0:
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    r_partial_sum = list(itertools.accumulate(r))
    b_partial_sum = list(itertools.accumulate(b))
    print(max(0, max(r_partial_sum)) + max(0, max(b_partial_sum)))
    t -= 1