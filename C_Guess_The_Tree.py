#author: Lemi
import sys

def query(u, v):
    print(f"? {u + 1} {v + 1}", flush=True)
    return it() - 1

def solve():
    n = it()
    
    edges = []
    c = list(range(n))

    def add_edge(u, v):
        edges.append((u, v))
        cand = [i for i in range(n) if c[i] == c[v]]
        for i in cand:
            c[i] = c[u]

    for _ in range(n - 1):
        u, v = 0, 0
        while c[v] == c[u]:
            v += 1
        
        while (x := query(u, v)) != u:
            if c[u] == c[x]:
                u = x
            else:
                v = x
        
        add_edge(u, v)

    print("!", " ".join(f"{u + 1} {v + 1}" for u, v in edges), flush=True)

t = it()
for _ in range(t):
    solve()
