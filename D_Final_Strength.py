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
    a = li()
    rounds = 2 ** n
    wins = [0] * rounds

    for i in range(n):
        for j in range(0, rounds, 2 ** (i + 1)):
            for k in range(2 ** i):
                p1 = j + k
                p2 = j + k + 2 ** i
                if a[p1] > a[p2]:
                    wins[p1] += 1
                elif a[p1] < a[p2]:
                    wins[p2] += 1

        for j in range(rounds):
            a[j] += wins[j]
            wins[j] = 0 

    print(*a)
 
 
t = it()
for _ in range(t):
    solve()


#



















# There are n
#  stages in a tournament. You are given an array a
#  of players' strength of length 2n
# .

# At every stage i
#  where 1≤i≤n
# , the following occurs:

# Consecutive 2i
#  players are grouped into one group. For example, in the first round, each group consists of 2
#  players (a1,a2),(a3,a4),...,(an−1,an)
# . In the second round, each group will consist of 4 consecutive players (a1,a2,a3,a4),...,(an−3,an−2,an−1,an)
# , and so forth.
# All players within their respective groups face off against each other if they haven't already in previous rounds. The player with the higher strength wins, and if both players have equal strength, neither wins.
# After that round finishes, every player's strength is increased by the number of wins they had in that round.
# Print the strength of all the players after the nth
#  stage.

# Input
# The first line contains a single integer t
#  where 1≤t≤104
#  — the number of test cases. The descriptions of the test cases follow.

# The first line of each test case contains n
#  where 1≤n≤17
# .

# The second line of each test case contains 2n
#  integers a1,a2,...,a2n(1≤ai≤109)
# .

# It is guaranteed that the sum of 2n
#  for all test cases does not exceed 2×105
# .

# Output
# For each test case, output 2n
#  numbers on a single line, separated by spaces, representing the final strength of each player.

# Example
# InputCopy
# 2
# 3
# 12 8 7 6 11 5 12 1
# 1
# 1 1
# OutputCopy
# 18 11 10 7 16 6 18 1
# 1 1
# Note
# Here are the groupings and the final strengths for all the rounds.

# Round	Group	Strength Before ith
#  Round	Strength After ith
#  Round
# 1
# 1
# [12,8]
# 2
# [7,6]
# 3
# [11,5]
# 4
# [12,1]
# [13,8,8,6,12,5,13,1]
# 2
# 1
# [13,8,8,6]
# 2
# [12,5,13,1]
# [15,9,8,6,13,6,15,1]
# 3
# 1
# [15,9,8,6,13,6,15,1]
# [18,11,10,7,16,6,18,1]
# Note that for round 2, player 1
#  will only play with players 3
#  and 4
#  since it has already played with player 2
#  in the first round. And for round 3
# , it will only play with players 5,6,7
# , and 8
#  since it has already played with player 2
#  in the first round and with players 3
#  and 4
#  in the second round. The same goes for all the players.
# # — Written by Solomon A.