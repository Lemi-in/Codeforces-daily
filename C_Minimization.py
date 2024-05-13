n, k = map(int, input().split())
lists = list(map(int, input().split()))
lists.sort()

i = 0
total = 0
while k > 0:
    while i < n and lists[i] - total == 0:
        i += 1

    if i < n and lists[i] - total > 0:
        print(lists[i] - total)
        total = lists[i]
    else:
        print(0)
    
    k -= 1



