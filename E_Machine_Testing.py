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
    h = li()
    p = li()
    time = 0
    for i in range(n - 1, 0, -1):
        h[i - 1] -= ceil(h[i] / p[i - 1]) * p[i - 1]
        time += ceil(h[i] / p[i - 1])
        if h[i - 1] <= 0:
            break
    print(time)

  
 
t = it()
for _ in range(t):
    solve()


















# Ras Makonnen Wolde Mikael is planning to design and develop a new set of guns. He has called for a nationwide initiative, inviting everyone to develop a new design of guns and bring a sample. Consequently, he has devised a test.

# Each gun has a health value hi
#  and power value pi
# . The power of each gun is measured by health points per second. This implies that a gun with power pi
#  decrements pi
#  health points from the gun it is shooting at, at the beginning of every second.

# To conduct the test, Ras Makonnen places n
#  guns in a line. Each gun is instructed to shoot at the gun directly in front of it. If a gun successfully reduces the health points of the gun in front of it to zero or below at the i
# -th second, the latter explodes at the i
# -th second, and the former proceeds to shoot at the next gun in line at the (i+1)
# -th second.

# Image for example testcase 1
# NB: A gun will shoot at the gun directly in front of it right before it explodes. For example, the second gun explodes at 2
#  seconds, but it has managed to shoot at the third gun, reducing its health by 1
#  point. Starting from 3
#  seconds, the first gun will shoot the third gun.

# Ras Makonnen seeks to determine the time it takes before all guns explode, except for the first one.

# Input
# The first line of the input contains an integer t
#  (1≤t≤104)
# , the number of test cases. For each test case:

# The first line contains an integer n
#  (1≤n≤105)
# , representing the number of guns.
# The second line contains n
#  integers h1,h2,…,hn
#  (1≤hi≤109)
# , denoting the health points of each gun.
# The third line contains n
#  integers p1,p2,…,pn
#  (1≤pi≤109)
# , denoting the power of each gun.
# It's guaranteed that the sum of n
#  over all the test cases does not exceed 2×105
# Output
# For each test case, print an integer representing the time it takes for all guns except the first one to explode.

# Example
# InputCopy
# 5
# 3
# 1 3 6
# 2 1 3
# 3
# 8 23 49
# 4 2 9
# 1
# 17
# 4
# 2
# 44 26
# 6 8
# 10
# 11 3 19 10 10 3 7 17 7 4
# 6 8 3 3 2 6 3 5 4 9
# OutputCopy
# 4
# 16
# 0
# 5
# 6
# Note
# For example testcase 1, refer to the above image.