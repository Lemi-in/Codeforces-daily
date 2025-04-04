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
 
def solve():
    n = it()
    count = 0
    freq = defaultdict(int)
    s = ' '.join([st() for _ in range(n)])
    for string in s.split():
        
        for i in range(2):
            for c in 'abcdefghijk':
    
                if string[i] != c:
                    modified = string[:i] + c + string[i+1:]
                    count += freq[modified]
        freq[string] += 1

    print(count)

 

t = it()
for _ in range(t):
    solve()

