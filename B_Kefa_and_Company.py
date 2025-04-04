
import sys
import heapq
import math
input = sys.stdin.readline
# sys.setrecursionlimit(100000)
# from collections import Counter, defaultdict
 
 
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def solve(n, d, array):
    array.sort()
    ans = array[0][1]
    l  = 0
    sum_ = ans
    
    for r in range(1,n):
        sum_ += array[r][1]
       
        while l < r and array[r][0] - array[l][0] >= d:
            
            sum_ -= array[l][1]
            l += 1
        
        ans = max(ans, sum_)
            
        
    
    return ans


n, d = inlt()
array = []

for _ in range(n):
    array.append(inlt())
print(solve(n, d, array))
    