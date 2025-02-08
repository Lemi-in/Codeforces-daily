from collections import Counter
#Template Author: Lemi
def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))


for _ in range(it()):
    s1 = s()
    t1 = s()
    p1 = s()
    
    i, j = 0, 0
    while i < len(s1) and j < len(t1):
        if s1[i] == t1[j]:
            i += 1
        j += 1
    if i < len(s1):
        print("NO")
        continue
    
    sCnt = Counter(s1)
    tCnt = Counter(t1)
    pCnt = Counter(p1)
    
    for char in tCnt:
        if tCnt[char] > sCnt.get(char, 0) + pCnt.get(char, 0):
            print("NO")
            break
    else:
        print("YES")
