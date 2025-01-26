def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def i(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

n = i()
arr = li()

if n <= 2:
    print(n)
    exit()

mx = 2  
curr = 2


for r in range(2, n):
    if arr[r] == arr[r-1] + arr[r-2]:
        curr += 1  
        mx = max(mx, curr)  
    else:
        curr = 2  

print(mx)
