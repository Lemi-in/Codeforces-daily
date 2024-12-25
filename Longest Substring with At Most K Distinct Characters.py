mp = {}
s = "aa"
n = len(s)
k = 1
l , mx = 0 , 0
for r in range(n):
    mp[s[r]] = mp.get(s[r], 0) + 1
    while len(mp) > k:
        mp[s[l]] -= 1
        if mp[s[l]] == 0:
            mp.pop(s[l])
        l += 1
    mx = max(mx , r - l + 1)
print(mx)