from collections import defaultdict

def dfs(u, parent, xor_value):
    global max_xor
    max_xor[u] = xor_value
    for v, w in tree[u]:
        if v != parent:
            dfs(v, u, xor_value ^ w)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tree = defaultdict(list)
    for _ in range(n - 1):
        v, u, w = map(int, input().split())
        tree[v].append((u, w))
        tree[u].append((v, w))

    max_xor = [-1] * (n + 1)
    dfs(1, 0, 0)

    queries = []
    for _ in range(m):
        query = input().split()
        if query[0] == '^':
            y = int(query[1])
            queries.append(('^', y))
        else:
            v, x = map(int, query[1:])
            queries.append(('?', v, x))

    cycle_xor = [max_xor[v] ^ x for _, v, x in queries if _ == '?']
    print(*cycle_xor)
