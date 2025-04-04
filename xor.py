from random import randint
from collections import Counter

arr = [1, 3,4,5,6,7,6,8,8,]
k = 2
mp = Counter()
rand = randint(1, 10 ** 5)

for a in arr:
    mp[a ^ rand] += 1
st = [key ^ rand for key, val in mp.items() if val >= k]