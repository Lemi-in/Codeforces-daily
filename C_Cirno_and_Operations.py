def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))
for _ in range(it()):
    n = it()
    a = li()
    a.reverse()
    smA = []
    smB = []

    if n == 1:
        print(a[0])
    else:
        
        for i in range(1 , n):
            smA.append(a[i] - a[i - 1])
        if len(smA) > 1:
            for i in range(1 , n):
                smB.append(smA[i] - smA[i - 1] )
        mx1 = max(sum(a), sum(smA))
        mx2 = max(max(a), max(smA))
        mx3 = float('-inf')
        if smB:
            mx3 = max(max(smB),sum(smB))
        print(max(mx1 , mx2, mx3))