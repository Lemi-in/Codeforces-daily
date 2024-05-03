import random
from functools import reduce
from operator import itemgetter

# define long long
#Python 3.6+
#compact version
def prod(nums): return reduce(lambda x,y:x*y, nums, 1)

t = int(input())
for _ in range(t):
    k, q = map(int, input().split())
    a = [int(input()) for _ in range(k)]
    ni = list(map(int, input().split()))
    winners = [0] * (max(a) + 1)
    for n in ni:
        players = list(range(1, n + 1))
        while players:
            kicked = set()
            for p in players:
                for a_i in a:
                    if p < a_i:
                        break
                    if p == a_i:
                        kicked.add(p)
            players = [p for p in players if p not in kicked]
            winners[min(kicked)] += 1 if kicked else 0
