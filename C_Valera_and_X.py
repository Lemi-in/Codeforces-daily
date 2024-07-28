n = int(input())
s = [input() for i in range(n)]

dgl = set()
non = set()

for i in range(n):
    for j in range(n):
        if i == j:
            dgl.add(s[i][j])
        elif j + 1 == n - i:
            dgl.add(s[i][j])
        else:
            non.add(s[i][j])
        if len(dgl) > 1 or len(non) > 1 or dgl == non: 
            print('NO')
            exit()
print('YES')