def ls(): return input().split()
def ints(): return map(int, input().split())
def it(): return int(input())

n, k = ints()
ropes = []

for _ in range(n):
    a = it()
    ropes.append(a)


l, r = 0, max(ropes)
mxRope = 0

def find(num):
    sm = 0
    for rope in ropes:
        sm += rope // num  
    return sm


while r - l > 1e-7:  
    mid = (l + r) / 2
    if find(mid) >= k:  
        mxRope = mid  
        l = mid  
    else:
        r = mid  

print(mxRope) 