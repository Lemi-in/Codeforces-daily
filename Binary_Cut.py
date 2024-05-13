def min_pieces(s):
    n = len(s)
    count_0 = 0
    count_1 = 0
    max_count = 0
    for i in range(n):
        if s[i] == '0':
            count_0 += 1
            max_count = max(max_count, count_1)
        else:
            count_1 += 1
            max_count = max(max_count, count_0)
    return max_count

t = int(input().strip())

for _ in range(t):
    s = input().strip()
    print(min_pieces(s))