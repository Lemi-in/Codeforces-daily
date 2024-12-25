items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]

items.sort(key=lambda x: (x[0], -x[1]))

n = len(items)
l, r = 0, 0
arr = []

while r < n:
    sm = 0
    cnt = 0
    avg = 0
    curr = items[l][0]
    
    while r < n and items[r][0] == curr and cnt < 5:
        sm += items[r][1]
        r += 1
        cnt += 1
    
    avg = sm // cnt if cnt > 0 else 0
    arr.append([curr, avg])

    while r < n and items[r][0] == curr:
        r += 1
    l = r

print(arr)
