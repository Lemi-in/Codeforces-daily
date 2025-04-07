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
    d = li()
    a = li()
    l = 1
    r = max(d)
    ans = -1
    def time(s):
        t = 0
        for i in range(n):
            if d[i] > 0:
                t += ceil(d[i] / s) * a[i]
        return t

    while l <= r:
        mid = (l + r) // 2
        
        if time(mid) <= k:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
            
    print(ans)

 
 
t = it()
for _ in range(t):
    solve()











# Empress Taytu Betul is an influential figure in the Battle of Adwa. Her brilliant mind swiftly devised a plan to cut off the Italians' water supply, thereby transforming their fort into a prison. However, one problem arose along with it. n
#  villages along the way will also suffer from a lack of water.

# Empress Taytu wants to fix this problem by using a horse-drawn wagon to transport water. The capacity of the wagon's tank determines its size; for instance, a wagon with size 2
#  can carry up to 2
#  liters of water.

# Each village's water demand is represented by an array d
# , denoting the required liters, while another array a
#  indicates the time it takes for the wagon to deliver water to a village and return to the source.

# Regrettably, the tank discharges all its water upon opening, allowing the wagon to supply water to only one village per trip. Consequently, if a wagon of size s
#  visits the i
# -th village with demand di
# , the village's water requirement decreases by s
#  liters, i.e., di:=di−s
# . If di
#  becomes negative, it indicates a surplus of water in the village.

# Empress Taytu is happy when all villages have non-positive demand, and the wagon is returned to the water source within no more than k
#  hours.

# Write a program to determine the minimum size of the wagon needed to make Empress Taytu happy. If it's impossible with any size of wagon, print −1
# .

# Input
# The input consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤1000)
# , the number of test cases. For each test case:

# The first line contains two integers n
#  and k
#  (1≤n≤105,1≤k≤1018)
# .
# The second line contains n
#  integers d1,d2,…,dn
#  (1≤di≤5×108)
# , denoting the water demand of each village.
# The third line contains n
#  integers a1,a2,…,an
#  (1≤ai≤105)
# , representing the time in hours it takes for the wagon to deliver water to each village and return to the water source.
# It is guaranteed that the sum of n
#  over all test cases does not exceed 105
# .
# Output
# Print a single integer, the minimum size of the wagon needed to make Empress Taytu happy. Print −1
#  if it is impossible with any size of wagon.

# Example
# InputCopy
# 5
# 3 12
# 4 1 7
# 5 1 2
# 4 65
# 6 2 5 3
# 13 5 12 10
# 5 100
# 40 53 20 13 1
# 20 11 10 23 40
# 1 1000000000000000000
# 500000000
# 100000
# 1 1
# 1
# 1
# OutputCopy
# 4
# 3
# -1
# 1
# 1
# Note
# For the first test case in the example, one of the possible ways to transport the water using a 4
# -sized wagon within 12
#  hours is:

# Deliver water to village 1
#  and return to the source in 5
#  hours. The new demand of all villages will be [0,1,7]
# .
# Deliver water to village 2
#  and return to the source in 1
#  hour. The new demand of all villages will be [0,−3,7]
# .
# Deliver water to village 3
#  and return to the source in 2
#  hours. The new demand of all villages will be [0,−3,3]
# .
# Deliver water to village 3
#  and return to the source in 2
#  hours. The new demand of all villages will be [0,−3,−1]
# .
# Now, all villages have non-positive demand. Totally, it takes 5+1+2+2=10
#  hours. Since it's not more than 12
#  hours, we can make Empress Taytu happy using a 4
# -sized wagon. It can be shown that we can't achieve this with any lower sizes.

# # — Written by Nardos W