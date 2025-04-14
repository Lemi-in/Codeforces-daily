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

from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

 
def solve():
    n , m = ints()
    a = [li() for _ in range(n)]
    vis = [[0] * m for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    #solve the problem using iterative approach
    def dfs(x, y):
        stack = [(x, y)]
        vis[x][y] = 1
        s = 1
        while stack:
            x, y = stack.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and a[nx][ny] == '.':
                    vis[nx][ny] = 1
                    stack.append((nx, ny))
                    s += 1
        return s

    ans = []
    for i in range(n):
        for j in range(m):
            if not vis[i][j] and a[i][j] == '.':
                sm = dfs(i, j)
                ans.append(sm)
    ans.sort(reverse=True)
    print(sum(ans[1:]))
    



    
 
 
t = it()
for _ in range(t):
    solve()

