def ls(): return input().split()
def ints(): return map(int, input().split())
def strs():return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

n , k = ints()
arr = li()
queries = li()

def find(num , arr):
    n = len(arr)
    l , r = 0 , n - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= num:
            ans = mid + 1
            l = mid + 1
        else:
            r = mid - 1
    print(ans)

for q in queries:
    find(q, arr)