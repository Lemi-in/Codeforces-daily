def ls(): return input().split()
def ints(): return map(int, input().split())
def strs():return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

for _ in range(it()):
    arr = []
    a,b,c = ints()
    if a + b == c:
        print('YES')
    elif a + c == b:
        print('YES')
    elif b + c == a:
        print('YES')
    else:
        print('NO')
    