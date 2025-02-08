def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

for _ in range(it()):
    n = it()
    arr = li()
    idx = 0
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            idx = i
    if idx == 0:  
        print("YES")
        continue

    for i in range(idx):
        mn = min(arr[i], arr[i + 1])
        arr[i] -= mn
        arr[i + 1] -= mn

    print("YES" if arr == sorted(arr) else "NO")
