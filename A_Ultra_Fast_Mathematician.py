
# Link: https://codeforces.com/problemset/problem/61/A
# Brute Force Approach has a time complexity of O(n) where n is the length of the string. and the space complexity is O(n) as well.
s = input()
t = input()
a = []
for i in range(len(s)):
    if s[i] != t[i]:
        a.append(1)
    else:
        a.append(0)
a = ''.join(map(str, a))

print(a)

# Optimized Approach has a time complexity of O(n) where n is the length of the string. and the space complexity is O(1).
s = input()
t = input()
for i in range(len(s)):
    if s[i] != t[i]:
        print(1, end='')
    else:
        print(0, end='')
   

   
