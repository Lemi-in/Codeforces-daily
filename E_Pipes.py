import sys
from collections import Counter, defaultdict,deque
from math import floor,ceil,sqrt
from random import randint
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp(): return int(input().strip())
def inlt(): return list(map(int, input().split()))
def insr(): return list(input().strip())
def invr(): return map(int, input().split())
rand = randint(1,10^6)
xor = lambda x: x^rand

############ ---- Solution Function ---- ############
def solve():
    n = inp()
    row1 = insr()
    row2 = insr()
    r,c = 1,n-1
    wred = True
    while c >= 0:
        if r:
            if row2[c] == '1' or row2[c] == '2':
                wred = True
                c -= 1
                continue
            if row1[c] == '1' or row1[c] == '2':
                return 'NO'
            if wred:
                c += 1
                wred = False
                r = 0
            else:
                wred = True
        else:
            if row1[c] == '1' or row1[c] == '2':
                wred = True
                c -= 1
                continue
            if row2[c] == '1' or row2[c] == '2':
                return 'NO'
            if wred:
                c += 1
                wred = False
                r = 1
            else:
                wred = True
        c -= 1
    if r == 0:
        return 'YES'
        
    return 'NO'
############ ---- Main Function ---- ############
def main():
    t = inp()  
    results = []
    for _ in range(t):
        results.append(solve())
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()