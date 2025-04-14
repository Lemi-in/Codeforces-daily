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
    n = it()
    edges = [tuple(ints()) for _ in range(n - 1)]
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    children = [[] for _ in range(n + 1)]
    q1 = deque([1])
    visited[1] = True
    while q1:
        u = q1.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                children[u].append(v)
                q1.append(v)

    cnt = [0] * (n + 1)
    @bootstrap
    def dfs(u):
        if not children[u]:
            cnt[u] = 1
        else:
            for c in children[u]:
                yield dfs(c)
                cnt[u] += cnt[c]
        yield 
    dfs(1)

    m = it()
    for _ in range(m):
        x, y = li()
        print(cnt[x] * cnt[y])
    
    
 
 
t = it()

for _ in range(t):
    solve()
