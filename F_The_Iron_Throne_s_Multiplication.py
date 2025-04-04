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
    l , r = 0, 0
    def helper(x):
        count = 0
        for i in range(1, n + 1):
            count += min(x // i, m)
        return count

        

    l, r = 1, n * m
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if helper(mid) >= k:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)
 
 
t = 1
for _ in range(t):
    solve()







#     Lord Varys the Champion isn't just charming, he also is very smart.

# While some of us were learning the multiplication table, Lord Varys the Champion had fun in his own manner. Lord Varys the Champion painted an n×m
#  multiplication table, where the element on the intersection of the i
# -th row and j
# -th column equals i⋅j
#  (the rows and columns of the table are numbered starting from 1). Then he was asked: what number in the table is the k
# -th largest number? Lord Varysthe Champion always answered correctly and immediately. Can you repeat his success?

# Consider the given multiplication table. If you write out all n⋅m
#  numbers from the table in the non-decreasing order, then the k
# -th number you write out is called the k
# -th largest number.

# Input
# The single line contains integers n
# , m
#  and k
#  (1≤n,m≤5⋅105; 1≤k≤n⋅m)
# .

# Output
# Print the k
# -th largest number in a n×m
#  multiplication table.

# Examples
# InputCopy
# 2 2 2
# OutputCopy
# 2
# InputCopy
# 2 3 4
# OutputCopy
# 3
# InputCopy
# 1 10 5
# OutputCopy
# 5
# Note
# A 2×3
#  multiplication table looks like this:


# 1 2 3
# 2 4 6

