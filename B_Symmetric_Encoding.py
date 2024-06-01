
t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    b = input().strip()
    distinct_chars = sorted(set(b))
    r = ''.join(distinct_chars)
    
    symmetric_map = {}
    len_r = len(r)
    for i in range(len_r):
        symmetric_map[r[i]] = r[len_r - 1 - i]
    
    s = ''.join(symmetric_map[char] for char in b)
    
    results.append(s)
for result in results:
    print(result)
