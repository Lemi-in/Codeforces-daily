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
 
 
t = 1
for _ in range(t):
    solve()

def add(fen, x, val, maxn):
    i = x + 1
    while i < maxn:
        fen[i] += val
        i += i & -i

def get(fen, x):
    ans = 0
    i = x
    while i > 0:
        ans += fen[i]
        i -= i & -i
    return ans

def sum_range(fen, x, y):
    return get(fen, y) - get(fen, x)

def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:]))
    
    maxn = 1000000 + 10
    fen = [0] * maxn
    cnt = [0] * maxn
    rem = [0] * n
    
    tot = sorted(set(a))
    
    a = [bisect_left(tot, x) for x in a]
    
    for i in range(n - 1, -1, -1):
        cnt[a[i]] += 1
        add(fen, cnt[a[i]], 1, maxn)
        rem[i] = cnt[a[i]]
    
    cnt = [0] * maxn
    ans = 0
    
    for i in range(n):
        add(fen, rem[i], -1, maxn)
        cnt[a[i]] += 1
        ans += sum_range(fen, 1, cnt[a[i]])
    
    print(ans)
    
if __name__ == "__main__":
    main()
