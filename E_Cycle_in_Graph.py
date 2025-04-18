#author: Lemi
import sys, heapq,math
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
from random import randint
from collections import defaultdict

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
    n ,m , k = ints()

    edges = []
    graph = defaultdict(list)
    for _ in range(m):
        a, b = ints()
        edges.append((a, b))
        graph[a].append(b)
        graph[b].append(a)

    @bootstrap
    def find(node, parent, visited, path):
        visited[node] = True
        path.append(node)

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if visited[neighbor]:
                start = path.index(neighbor)
                cycle = path[start:]
                if len(cycle) >= k + 1:
                    print(len(cycle))
                    print(" ".join(map(str, cycle)))
                    sys.exit(0)
            else:
                yield find(neighbor, node, visited, path)

        path.pop()

    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            find(i, -1, visited, [])


 
t = 1
for _ in range(t):
    solve()

























# You've got a undirected graph G, consisting of n nodes. We will consider the nodes of the graph indexed by integers from 1 to n. We know that each node of graph G is connected by edges with at least k other nodes of this graph. Your task is to find in the given graph a simple cycle of length of at least k + 1.

# A simple cycle of length d (d > 1) in graph G is a sequence of distinct graph nodes v1, v2, ..., vd such, that nodes v1 and vd are connected by an edge of the graph, also for any integer i (1 ≤ i < d) nodes vi and vi + 1 are connected by an edge of the graph.

# Input
# The first line contains three integers n, m, k (3 ≤ n, m ≤ 105; 2 ≤ k ≤ n - 1) — the number of the nodes of the graph, the number of the graph's edges and the lower limit on the degree of the graph node. Next m lines contain pairs of integers. The i-th line contains integers ai, bi (1 ≤ ai, bi ≤ n; ai ≠ bi) — the indexes of the graph nodes that are connected by the i-th edge.

# It is guaranteed that the given graph doesn't contain any multiple edges or self-loops. It is guaranteed that each node of the graph is connected by the edges with at least k other nodes of the graph.

# Output
# In the first line print integer r (r ≥ k + 1) — the length of the found cycle. In the next line print r distinct integers v1, v2, ..., vr (1 ≤ vi ≤ n) — the found simple cycle.

# It is guaranteed that the answer exists. If there are multiple correct answers, you are allowed to print any of them.

# Examples
# InputCopy
# 3 3 2
# 1 2
# 2 3
# 3 1
# OutputCopy
# 3
# 1 2 3 
# InputCopy
# 4 6 3
# 4 3
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# OutputCopy
# 4
# 3 4 1 2 

