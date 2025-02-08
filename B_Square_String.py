def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

for _ in range(it()):
    t = s()
    n = len(t)
    if n % 2 != 0:
        print('NO')
    else:
        m = n // 2
        if t[:m] == t[m:]:
            print('YES')
        else:
            print('NO')