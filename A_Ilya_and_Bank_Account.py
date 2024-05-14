# # Link: https://codeforces.com/problemset/problem/313/A
# #Brute force solution. Time complexity is O(n) and space complexity is O(n)
# o = input()
# intO = int(o)
# c = list(o)
# n = len(c)
# l = []
# s  = []

# for j in range(n - 1):
#     l.append(c[j])

# for j in range(n):
#     if j == n - 2:
#         pass
#     else:
#         s.append(c[j])

# l = ''.join(l)
# s = ''.join(s)
# l = int(l)
# s = int(s)
# maxx = max(l,s)
# if intO > maxx:
#     print(intO)
# else:
#     print(maxx)


#Optimal Solution. Time complexity is O(1) and spa
n = int(input())
Max = n
if n // 10 > Max:
    Max = n // 10

if n % 10 + ((n // 100) * 10) > Max:
    Max = n % 10 + ((n // 100) * 10)
print(Max)
