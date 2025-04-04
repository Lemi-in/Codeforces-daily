def solve():
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    print(max(A), max(B))

# Read input and solve
solve()
