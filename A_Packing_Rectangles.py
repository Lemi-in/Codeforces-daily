def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))


w, h, n = ints()


l, r = max(w, h), n * max(w, h)
ans = 10**9
while l <= r:
    mid = (l + r) // 2
   
    total = (mid // w) * (mid // h)
    if total >= n:
        r = mid - 1
    else:
        l = mid + 1
print(l)

