from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))
 
def find(n, k, a):
    l, r = 0, 0
    cnt = 0
    mp = defaultdict(int)
    dcnt = 0
    
    while r < n:
        mp[a[r]] += 1
        if mp[a[r]] == 1: dcnt += 1
        while dcnt > k:
            mp[a[l]] -= 1
            dcnt -= (mp[a[l]] == 0)
            l += 1
        cnt += (r - l + 1)
        r += 1
    
    return cnt


print(find(n, k, arr)) 
