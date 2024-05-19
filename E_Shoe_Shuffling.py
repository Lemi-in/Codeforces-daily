from itertools import permutations
t = int(input())

for _ in range(t):
    n = int(input())
    shoes = list(map(int, input().split()))


    ans = []
    for i in range(1, n + 1):
        ans.append(i)
    l = 0
    r = 0
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

# from collections import defaultdict

# t = int(input())
# for _ in range(t):
#   n = int(input())
#   a = list(map(int,input().split()))
#   table = defaultdict(int)

#   for i in a:
#     table[i] += 1

#  # print(table, table.values(), "\n")

#   if 1 in table.values():
#     print(-1)
#   else:
#     tmp = 0
#     for k in table:
#       print(tmp + table[k], end=' ')
#       for j in range(tmp + 1,tmp + table[k]):
#         print(j,end=' ')
#       tmp += table[k]
