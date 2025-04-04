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
    s = st()
    
    free_rooms = [i for i, c in enumerate(s) if c == '0']
    free = [i for i, c in enumerate(s) if c == '0']
    min_distance = float('inf')

    for i in range(len(free_rooms) - k):
        mid = (free_rooms[i] + free_rooms[i + k]) // 2
        max_dist = max(abs(free_rooms[i] - mid), abs(free_rooms[i + k] - mid))
        min_distance = min(min_distance, max_dist)

    
    mn = float('inf')

    for i in range(len(free) - k):
        mid = (free[i] + free[i + k]) // 2
        max_dist = max(abs(free[i] - mid), abs(free[i + k] - mid))
        mn = min(mn, max_dist)

    print(mn)
    
 
 
t = 1
for _ in range(t):
    solve()










#     In an attempt to escape the Mischievous Mess Makers' antics, Farmer John has abandoned his farm and is traveling to the other side of Bovinia. During the journey, he and his k
#  cows have decided to stay at the luxurious Grand Moo-dapest Hotel. The hotel consists of n
#  rooms located in a row, some of which are occupied.

# Farmer John wants to book a set of k+1
#  currently unoccupied rooms for him and his cows. He wants his cows to stay as safe as possible, so he wishes to minimize the maximum distance from his room to the room of his cow. The distance between rooms i
#  and j
#  is defined as |j−i|
# . Help Farmer John protect his cows by calculating this minimum possible distance.

# Input
# The first line of the input contains two integers n
#  and k
#  (1≤k<n≤100000
# ) — the number of rooms in the hotel and the number of cows travelling with Farmer John.

# The second line contains a string of length n
#  describing the rooms. The i
# -th character of the string will be '0' if the i
# -th room is free, and '1' if the i
# -th room is occupied. It is guaranteed that at least k+1
#  characters of this string are '0', so there exists at least one possible choice of k+1
#  rooms for Farmer John and his cows to stay in.

# Output
# Print the minimum possible distance between Farmer John's room and his farthest cow.

# Examples
# InputCopy
# 7 2
# 0100100
# OutputCopy
# 2
# InputCopy
# 5 1
# 01010
# OutputCopy
# 2
# InputCopy
# 3 2
# 000
# OutputCopy
# 1
# Note
# In the first sample, Farmer John can book room 3
#  for himself, and rooms 1
#  and 4
#  for his cows. The distance to the farthest cow is 2
# . Note that it is impossible to make this distance 1
# , as there is no block of three consecutive unoccupied rooms.

# In the second sample, Farmer John can book room 1
#  for himself and room 3
#  for his single cow. The distance between him and his cow is 2
# .

# In the third sample, Farmer John books all three available rooms, taking the middle room for himself so that both cows are next to him. His distance from the farthest cow is 1
# .