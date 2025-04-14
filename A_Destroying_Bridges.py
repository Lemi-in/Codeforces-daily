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
    n , k = ints()
    
 
t = it()
for _ in range(t):
    solve()





#solve 
# There are n
#  islands, numbered 1,2,…,n
# . Initially, every pair of islands is connected by a bridge. Hence, there are a total of n(n−1)2
#  bridges.

# Everule lives on island 1
#  and enjoys visiting the other islands using bridges. Dominater has the power to destroy at most k
#  bridges to minimize the number of islands that Everule can reach using (possibly multiple) bridges.

# Find the minimum number of islands (including island 1
# ) that Everule can visit if Dominater destroys bridges optimally.

# Input
# Each test contains multiple test cases. The first line contains a single integer t
#  (1≤t≤103
# ) — the number of test cases. The description of the test cases follows.

# The first and only line of each test case contains two integers n
#  and k
#  (1≤n≤100
# , 0≤k≤n⋅(n−1)2
# ).

# Output
# For each test case, output the minimum number of islands that Everule can visit if Dominater destroys bridges optimally.

# Example
# InputCopy
# 6
# 2 0
# 2 1
# 4 1
# 5 10
# 5 3
# 4 4
# OutputCopy
# 2
# 1
# 4
# 1
# 5
# 1
# Note
# In the first test case, since no bridges can be destroyed, all the islands will be reachable.

# In the second test case, you can destroy the bridge between islands 1
#  and 2
# . Everule will not be able to visit island 2
#  but can still visit island 1
# . Therefore, the total number of islands that Everule can visit is 1
# .

# In the third test case, Everule always has a way of reaching all islands despite what Dominater does. For example, if Dominater destroyed the bridge between islands 1
#  and 2
# , Everule can still visit island 2
#  by traveling by 1→3→2
#  as the bridges between 1
#  and 3
# , and between 3
#  and 2
#  are not destroyed.

# In the fourth test case, you can destroy all bridges since k=n⋅(n−1)2
# . Everule will be only able to visit 1
#  island (island 1
# ).


