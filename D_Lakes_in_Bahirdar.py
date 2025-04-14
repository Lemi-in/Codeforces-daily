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
    n , m , k = ints()
    a = [list(st()) for _ in range(n)]
    def check(x, y):
        return x == 0 or y == 0 or x == n - 1 or y == m - 1

    def dfs(x, y, lake_id):
        stack = [(x, y)]
        lake = []
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited or a[cx][cy] == '*':
                continue
            visited.add((cx, cy))
            lake.append((cx, cy))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m:
                    stack.append((nx, ny))
        return lake

    visited = set()
    lakes = []
    bLakes = set()

    for i in range(n):
        for j in range(m):
            if (i, j) not in visited and a[i][j] == '.':
                lake = dfs(i, j, len(lakes))
                if any(check(x, y) for x, y in lake):
                    bLakes.update(lake)
                else:
                    lakes.append(lake)

    lakes.sort(key=len)
    cells = 0
    for i in range(len(lakes) - k):
        cells += len(lakes[i])
        for x, y in lakes[i]:
            a[x][y] = '*'

    print(cells)
    for row in a:
        print(''.join(row))
    
    
 
 
t = 1
for _ in range(t):
    solve()






















# The map of Bahirdar is a rectangle of the size n×m
# , which consists of cells of size 1×1
# . Each cell is either land or water. The map is surrounded by the ocean.

# Lakes are the maximal regions of water cells, connected by sides, which are not connected with the ocean. Formally, lake is a set of water cells, such that it's possible to get from any cell of the set to any other without leaving the set and moving only to cells adjacent by the side, none of them is located on the border of the rectangle, and it's impossible to add one more water cell to the set such that it will be connected with any other cell.

# You task is to fill up with the earth the minimum number of water cells so that there will be exactly k
#  lakes in Bahirdar. Note that the initial number of lakes on the map is not less than k
# .

# Input
# The first line of the input contains three integers n
# , m
#  and k
#  (1≤n,m≤50
# , 0≤k≤50
# ) — the sizes of the map and the number of lakes which should be left on the map.

# The next n
#  lines contain m
#  characters each — the description of the map. Each of the characters is either '.' (it means that the corresponding cell is water) or '*' (it means that the corresponding cell is land).

# It is guaranteed that the map contain at least k
#  lakes.

# Output
# In the first line print the minimum number of cells which should be transformed from water to land.

# In the next n
#  lines print m
#  symbols — the map after the changes. The format must strictly follow the format of the map in the input data (there is no need to print the size of the map). If there are several answers, print any of them.

# It is guaranteed that the answer exists on the given data.

# Examples
# InputCopy
# 5 4 1
# ****
# *..*
# ****
# **.*
# ..**
# OutputCopy
# 1
# ****
# *..*
# ****
# ****
# ..**
# InputCopy
# 3 3 0
# ***
# *.*
# ***
# OutputCopy
# 1
# ***
# ***
# ***
# Note
# In the first example there are only two lakes — the first consists of the cells (2,2)
#  and (2,3)
# , the second consists of the cell (4,3)
# . It is profitable to cover the second lake because it is smaller. Pay attention that the area of water in the lower left corner is not a lake because this area share a border with the ocean.