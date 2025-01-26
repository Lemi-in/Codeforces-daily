def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

for _ in range(it()):
    n , k = ints()
    a = li()
    a.sort()
    l , r = 0 , n - 1
    cnt = 0
    while l < r:
        sm = a[l] + a[r]
        if sm == k:
            cnt += 1
            r -= 1
            l += 1
        elif sm > k:
            r -= 1
        else:
            l += 1
    print(cnt)