#author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from random import randint

rand = randint(1, 10**5)
def ran(num): return num ^ rand
def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def st(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 
 

n = it()
xs = []
ys = []
zs = []
 
for _ in range(n):
    x, y, z = ints()
    xs.append(x)
    ys.append(y)
    zs.append(z)
 
outs = []
 
def solve1(lst): 
    lst.sort(key=lambda x: zs[x])
    while len(lst) >= 2:
        x, y = lst.pop(), lst.pop()
        outs.append(f'{x + 1} {y + 1}')
    return lst
    
def solve2(lst):
    lst.sort(key=lambda x: ys[x])
    resid = []
    tmp = []
    for i in lst:
        if len(tmp) == 0 or ys[i] == ys[tmp[0]]:
            tmp.append(i)
        else:
            resid.extend(solve1(tmp))
            tmp = [i]
    resid.extend(solve1(tmp))
    while len(resid) >= 2:
        x, y = resid.pop(), resid.pop()
        outs.append(f'{x + 1} {y + 1}')
    return resid
 
def solve3(lst):
    lst.sort(key=lambda x: xs[x])
    resid = []
    tmp = []
    for i in lst:
        if len(tmp) == 0 or xs[i] == xs[tmp[0]]:
            tmp.append(i)
        else:
            resid.extend(solve2(tmp))
            tmp = [i]
    resid.extend(solve2(tmp))
    while len(resid) >= 2:
        x, y = resid.pop(), resid.pop()
        outs.append(f'{x + 1} {y + 1}')
 
solve3(list(range(n)))
print('\n'.join(outs))