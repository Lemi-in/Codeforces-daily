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
 

def is_spruce():
    n = it()
    parents = []
    for _ in range(n - 1):
        p = it()
        parents.append(p)
    
    tree = {i: [] for i in range(1, n + 1)}
    
    #the following 
    
    for child, parent in enumerate(parents, start=2):
        tree[parent].append(child)
  
    for node in range(1, n + 1):
        if tree[node]:  
            cnt = sum(1 for child in tree[node] if not tree[child])
            if cnt < 3:
                print("No")
                return
    
    print("Yes")

is_spruce()
