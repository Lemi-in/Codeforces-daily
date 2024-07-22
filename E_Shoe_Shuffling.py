# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     cnt = {}
#     for i in arr:
#         if i in cnt:
#             cnt[i] += 1
#         else:
#             cnt[i] = 1
#     if all(x > 1 for x in cnt.values()):
#         res = [i for i in range(1, n + 1)]
#         def backtrack(res, path):
#             if len(path) == n:
#                 temp = [x for x, y in enumerate(path, 1) if x != y and arr[y - 1] <= arr[x - 1]]
#                 if len(temp) == n:
#                     print(*path)
#                     return True
#                 return False
#             for i in range(len(res)):
#                 if backtrack(res[:i] + res[i + 1:], path + [res[i]]):
#                     return True
#             return False
#         backtrack(res, [])
#     else:
#         print(-1)

t = int(input())
for _ in range(t):
    n = int(input())
    shoes = list(map(int, input().split()))
 
    ans = [i for i in range(1 , n + 1)]
 
    l , r = 0 , 0
    permut = True
 
    while r < n:
        while r < n - 1 and shoes[r] == shoes[r + 1]: 
            r += 1
        if l == r:
            permut = False
        else:
            temp = ans[l+1:r+1]  
            temp.append(ans[l])  
            ans[l:r+1] = temp  
        l = r + 1
        r += 1
 
    if permut:
        print(*ans)
    else:
        print(-1)

        