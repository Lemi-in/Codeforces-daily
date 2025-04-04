# Template Author: Lemi
import sys, heapq, math
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
    with open("input.txt", "r") as inPut:
        n = int(inPut.readline().strip())
        arr = list(map(int, inPut.readline().split()))

    mx = n
    positives = [0] * n
    negatives = [0] * n

    positives[0] += (arr[0] >= 0)
    for i in range(1, n):
        positives[i] = positives[i - 1] + (arr[i] >= 0)

    negatives[n - 1] += (arr[n - 1] <= 0 )

    for i in range(n - 2, -1, -1):
        negatives[i] = negatives[i + 1] + (arr[i] <= 0 )


    for i in range(n - 1):
        mx = min(mx, positives[i] + negatives[i + 1])

    with open("output.txt", "w") as outPut:
        outPut.write(str(mx) + "\n")

t = 1
for _ in range(t):
    solve()

