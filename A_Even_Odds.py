# Link: https://codeforces.com/contest/318/problem/A
# To solve this problem, I had to come up with 3 different solutions. Isn't that interesting?
# Bruteforce solution has time complexity of O(n) and space complexity of O(n)
n, k = map(int, input().split())
evenOdd  = []
for i in range(1,n+1):
    if i % 2 != 0:
        evenOdd.append(i)
for i in range(1,n+1):
    if i % 2 == 0:
        evenOdd.append(i)
print(evenOdd[k-1])

# Better Solution but has time complexity of O(n)

n , k = map(int, input().split())
odd = 1
even = 1
secondHalf= n // 2
if n % 2 == 0:
    m = k - secondHalf
else:
    m = k - secondHalf- 1

if k <= secondHalf:
    for i in range(1,n + 1,2):
        if odd == k:
            print(i)
            break
        odd += 1

else:
    for i in range(2,n + 1,2):
        if even == m:
            print(i)
            break
        even += 1

# Optimal Solution but has time complexity of O(1) and space complexity of O(1)
n, k = map(int, input().split())
if n % 2 == 0:  
    if k <= n // 2:
        print(k * 2 - 1)
    else:
        print((k - n // 2) * 2)
else:  
    if k <= n // 2 + 1:
        print(k * 2 - 1)
    else:
        print((k - n // 2 - 1) * 2)


