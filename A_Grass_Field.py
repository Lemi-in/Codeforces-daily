# Template Author: Lemi
import sys
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
 
    x, y = ints()
    i, j = ints()

    total = x + y + i + j

    if total == 0:
        print(0)
    elif total == 4:
        print(2)
    else:
        print(1)


t = it()
for _ in range(t):
    solve()
