def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])  # Number of nodes
    edges = data[1:]  # Edges of the tree
    
    # Degree array to count the degree of each node
    degree = [0] * (n + 1)
    
    # Process edges

    for edge in edges:
        u, v = map(int, edge.split())
        degree[u] += 1
        degree[v] += 1
    
    # Count leaf nodes (nodes with degree 1)
    leaf_count = sum(1 for d in degree if d == 1)
    
    # If the number of leaves is odd, output NO; otherwise, YES
    if leaf_count % 2 == 1:
        print("NO")
    else:
        print("YES")

solve()
