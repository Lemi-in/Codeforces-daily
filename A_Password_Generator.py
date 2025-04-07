#author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from random import randint, shuffle

rand = randint(1, 10**5)
def ran(num): return num ^ rand
def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def st(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
def yesNo(value): return 'YES' if value == 1 else 'NO' 

def solve():
    a, b, c = ints()

    digits = [str(i) for i in range(10)]
    upper = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    lower = [chr(i) for i in range(ord('a'), ord('z')+1)]

    res = []

    for i in range(a):
        res.append(digits[i % 10])
    for i in range(b):
        res.append(upper[i % 26])
    for i in range(c):
        res.append(lower[i % 26])


    for _ in range(100):
        shuffle(res)
        ok = True
        for i in range(1, len(res)):
            if res[i] == res[i - 1]:
                ok = False
                break
        if ok:
            break

    print(''.join(res))

t = it()
for _ in range(t):
    solve()
