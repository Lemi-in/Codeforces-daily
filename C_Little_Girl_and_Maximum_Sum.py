n , q = map(int, input().split())
arr = list(map(int, input().split()))
queries = []

for _ in range(q):
    l ,  r = map(int, input().split())
    queries.append([l , r])

def mx_sum(n, q, arr, queries):
    diff = [0] * (n + 2)
    for l, r in queries:
        diff[l] += 1
        diff[r + 1] -= 1
    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + diff[i]
    
    arr.sort(reverse=True)
    prefix = prefix[1:]
    prefix.sort(reverse=True)
    
    mx = 0
    for i in range(n):
        mx += arr[i] * prefix[i]
    
    return mx


print(mx_sum(n, q, arr, queries))  
