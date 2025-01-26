def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

for _ in range(it()):
    n = it()
    arr = li()
    ans = "YES"
    for i in range(n):
        if arr[i] <= (2 * (n - (i + 1))):

            ans = "NO"
            break       
    print(ans)