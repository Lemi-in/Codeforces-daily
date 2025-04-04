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
    s, b = ints()
    a = li()
    bases = []
    for _ in range(b):
        d, g = ints()
        bases.append((d, g))
    bases.sort()
    prefix_sum = [0] * (b + 1)
    for i in range(1, b + 1):
        prefix_sum[i] = prefix_sum[i - 1] + bases[i - 1][1]
    result = []
    for spaceship in a:
        left, right = 0, b - 1
        while left <= right:
            mid = (left + right) // 2
            if bases[mid][0] <= spaceship:
                left = mid + 1
            else:
                right = mid - 1
        result.append(prefix_sum[left])
    print(*result)
   
    
    
t = 1
for _ in range(t):
    solve()

 


# Arya Stark and The Hound hopped out of the TARDIS and found themselves at EPFL in 2018. They were surrounded by Lannister guards, and the Night King was approaching. Miraculously, they managed to escape to a nearby rebel base, but Arya was very confused. Heidi reminded her that last year's HC2 theme was Game of Thrones. Now she understood, and she's ready to face the evils of the White Walkers!

# The rebels have s
#  spaceships, each with a certain attacking power a
# .

# They want to send their spaceships to destroy the empire bases and steal enough gold and supplies in order to keep the rebellion alive.

# The empire has b
#  bases, each with a certain defensive power d
# , and a certain amount of gold g
# .

# A spaceship can attack all the bases which have a defensive power less than or equal to its attacking power.

# If a spaceship attacks a base, it steals all the gold in that base.

# The rebels are still undecided which spaceship to send out first, so they asked for the Doctor's help. They would like to know, for each spaceship, the maximum amount of gold it can steal.

# Input
# The first line contains integers s
#  and b
#  (1≤s,b≤105
# ), the number of spaceships and the number of bases, respectively.

# The second line contains s
#  integers a
#  (0≤a≤109
# ), the attacking power of each spaceship.

# The next b
#  lines contain integers d,g
#  (0≤d≤109
# , 0≤g≤104
# ), the defensive power and the gold of each base, respectively.

# Output
# Print s
#  integers, the maximum amount of gold each spaceship can steal, in the same order as the spaceships are given in the input.

# Example
# InputCopy
# 5 4
# 1 3 5 2 4
# 0 1
# 4 2
# 2 8
# 9 4
# OutputCopy
# 1 9 11 9 11
# Note
# The first spaceship can only attack the first base.

# The second spaceship can attack the first and third bases.

# The third spaceship can attack the first, second and third bases.