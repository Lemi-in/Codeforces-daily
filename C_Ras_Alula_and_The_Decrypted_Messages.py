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
    n, m = ints()
    s = st()
    w = st()
    
    s = [ord(c) - ord('a') for c in s]
    w = [ord(c) - ord('a') for c in w]

    s_count = [0] * 26
    w_count = [0] * 26

    for i in range(m):
        if s[i] != 25:
            s_count[s[i]] += 1
            w_count[w[i]] += 1
    for i in range(26):
        if s_count[i] < w_count[i]:
            print("NO")
            return
    for i in range(m, n):
        if s[i] != 25:
            s_count[s[i]] += 1
            s_count[s[i - m]] -= 1
            if s_count[s[i - m]] < w_count[s[i - m]]:
                print("NO")
                return
            if s_count[s[i]] < w_count[s[i]]:
                print("NO")
                return
 
   
    print("YES")

t = it()
for _ in range(t):
    solve()



















# Ras Alula Engida, the Ethiopian hero general, has intercepted a set of surrendered messages (with n
#  characters) from a group of infiltrated spies. These messages contain crucial information about the enemy's plans. Ras Alula aims to exploit this intelligence to gain a strategic advantage.

# Ras Alula discovered that the enemy employs a unique encryption technique for messages. For any given word b
#  that is present in the message, if there is at least one i
#  (1≤i≤n
# ) where bi≠
#  'z', they perform this operation:

# They choose an index i
#  (1≤i≤n
# ) where bi≠
#  'z'.
# They increment bi
#  ('a' to 'b', 'b' to 'c', ... 'y' to 'z')
# They choose an index j
#  (1≤j≤n
# ) where bj≠
#  'a'. Note that, they might choose the same i
#  and j
# .
# They decrement bj
#  ('b' to 'a', 'c' to 'b', ... 'z' to 'y').
# The enemy might perform the above operation any number of times on a given word. For example, one of the ways the enemy might encrypt "adwa" to "bcvb" in 3
#  operations is:

# Increment b1
# , b
#  becomes "bdwa". Decrement b3
# , b
#  becomes "bdva".
# Increment b4
# , b
#  becomes "bdvb". Decrement b2
# , b
#  becomes "bcvb".
# Increment b2
# , b
#  becomes "bdvb". Decrement b2
# , b
#  becomes "bcvb".
# After encrypting every word with some sequence of the operation, they concatenate each word to make one long string s
# .

# Ras Alula has this long encrypted string s
# . Unfortunately, Ras Alula couldn't determine the exact operation sequence. However, he wants to check if it is possible for s
#  to contain the word w
#  with length m
# .

# Assist Ras Alula by determining if it is possible for s
#  to contain the word w
# . Print "YES" if it does, "NO" otherwise.

# Input
# The first line contains an integer t
#  (1≤t≤104)
#  — the number of test cases.
# For each test case:
# The first line contains two integers n
#  and m
#  (1≤m≤n≤105)
#  — the length of the decrypted message s
#  and the length of the sensitive word w
# , respectively.
# The second line contains the decrypted message s
#  consisting of n
#  lowercase English letters.
# The third line contains the sensitive word w
#  consisting of m
#  lowercase English letters.
# It is guaranteed that the sum of n
#  over all test cases does not exceed 105
# .
# Output
# For each test case, print "YES" if it is possible for s
#  to contain the word w
# , "NO" otherwise.
# Example
# InputCopy
# 2
# 8 4
# aabcvbzb
# adwa
# 8 3
# xczyaxab
# abc
# OutputCopy
# YES
# NO
# Note
# In testcase 1
# , the string contains the substring "bcvb" that could have been encrypted from "adwa" with some sequence of operations, as shown in the above example.
# In testcase 2
# , there is no substring that could have been encrypted from "abc".
# — Written by 