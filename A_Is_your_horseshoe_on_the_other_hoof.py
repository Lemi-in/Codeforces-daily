# Brute force approach has a time complexity of O(n) where n is the length of the string. and the space complexity is O(n) as well.

colors = list(map(int, input().split()))
un = 0
for i in range(len(colors)):
    isUn = True
    for j in range(i + 1, len(colors)):
        if colors[i] == colors[j]:
            isUn = False
            break
    if isUn:
        un += 1
print(4 - un)


# Optimized Approach has a time complexity of O(n) where n is the length of the string. and the space complexity is O(1).
a = list(map(int, input().split()))
s = set(a)
print(4 - len(s))
