#author: Lemi
import sys
from math import inf

def it(): return int(sys.stdin.readline())
def li(): return list(map(int, sys.stdin.readline().split()))
def fmin(a, b): return a if a < b else b

t = it()
outs = []
for _ in range(t):
    n, k = li()
    nums = li()
    
    if k >= 3:
        outs.append(0)
    else:
        v = min(nums)
        nums.sort()
        for i in range(1, n):
            v = fmin(v, nums[i] - nums[i - 1])
        
        if k == 1:
            outs.append(v)
        else:
            for i in range(n):
                pt = 0
                for j in range(i, n):
                    cur = nums[i] + nums[j]
                    while pt < n and nums[pt] <= cur:
                        pt += 1
                    if pt < n: v = fmin(v, abs(nums[pt] - cur))
                    if pt: v = fmin(v, abs(nums[pt - 1] - cur))
            outs.append(v)

print('\n'.join(map(str, outs)))
