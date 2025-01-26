from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()
    mp = Counter(s)

    mx = max(mp.values())
    mn = min(mp.values())

    for t in s:
        if mp[t] == mx:
            mxl = t
            break


    lst = list(s)
    
    for i in range(n):
        if mp[lst[i]] == mn and lst[i] != mxl:
            lst[i] = mxl
            break
    print(''.join(lst))
