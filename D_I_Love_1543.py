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
 
def Layers(matrix):
    n, m = len(matrix), len(matrix[0])  
    layers = []  
    
    top, left, bottom, right = 0, 0, n - 1, m - 1  
    
    while top <= bottom and left <= right:
        layer = []  
        for i in range(left, right + 1):
            layer.append(matrix[top][i])

        for i in range(top + 1, bottom + 1):
            layer.append(matrix[i][right])
        
        if top != bottom:
            for i in range(right - 1, left - 1, -1):
                layer.append(matrix[bottom][i])
        
        if left != right:
            for i in range(bottom - 1, top, -1):
                layer.append(matrix[i][left])
        
        layers.append(layer)  
        
        top += 1
        left += 1
        bottom -= 1
        right -= 1
    
    return layers

def count(mat):
    cnt , l , = 0 , 0
    fav = '1543'
    for r in range(3, len(mat)):
        if ''.join(mat[l:r + 1]) == fav:
            cnt += 1
        l  += 1
        r += 1

    return cnt
    
def solve():
    n , m = ints()
    carpet = [s() for _ in range(n)]
    carpet = [list(c) for c in carpet]
    
    layers = Layers(carpet)
    layers = [m + m[:3] for m in layers]

    total = 0
    for m in layers:
        total += count(m)
    print(total)
   
  
    
 
t = it()
for _ in range(t):
    solve()