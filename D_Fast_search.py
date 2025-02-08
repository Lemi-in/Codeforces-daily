def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))
from bisect import bisect_left, bisect_right

n = it()
arr = li()
k = it()
queries = [tuple(ints()) for _ in range(k)]

arr.sort()

def find(l, r, arr):
    
    left = bisect_left(arr, l)
    right = bisect_right(arr, r)
    return right - left

ans = [find(l, r, arr) for l, r in queries]

print(*ans)
