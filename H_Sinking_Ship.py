# Template Author: Lemi
import sys
import heapq
import math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd

def ls(): return sys.stdin.readline().split()
def ints(): return map(int, sys.stdin.readline().split())
def strs(): return map(str, sys.stdin.readline().split())
def it(): return int(sys.stdin.readline())
def s(): return sys.stdin.readline().strip()
def li(): return list(map(int, sys.stdin.readline().split()))
 
def solve():
    n = it()
    rats = []
    woCh = []
    man = []
    cap = []
    for _ in range(n):
        name, tag = strs()
        if tag == "rat":
            rats.append(name)
        elif tag == "man":
            man.append(name)
        elif tag == 'captain':
            cap.append(name)
        else:
            woCh.append(name)
    ans = []
    ans.extend(rats)
    ans.extend(woCh)
    ans.extend(man)
    ans.extend(cap)
    for a in ans:
        print(a)

 
 
t = 1
for _ in range(t):
    solve()