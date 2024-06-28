t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    
    a_rows = [''.join(map(str, sorted(row))) for row in a]
    a_cols = [''.join(map(str, sorted([row[i] for row in a]))) for i in range(m)]
    b_rows = [''.join(map(str, sorted(row))) for row in b]
    b_cols = [''.join(map(str, sorted([row[i] for row in b]))) for i in range(m)]
    
    if sorted(a_rows) == sorted(b_rows) and sorted(a_cols) == sorted(b_cols):
        print("YES")
    else:
        print("NO")