def min_health_decrement(n, attacks, edges):
    from collections import defaultdict, deque
    
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # DP array and visited set
    dp = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    def dfs(node):
        visited[node] = True
        dp[node] = attacks[node - 1]  # Initialize with the monster's attack points
        max_single = 0
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                max_single = max(max_single, dp[neighbor])
        
        dp[node] += max_single
    
    # Start DFS from node 1 (or any arbitrary root)
    dfs(1)
    
    # The result is the maximum of dp values of all nodes
    return sum(dp) - max(dp)

# Read input and process each test case
import sys
input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    attacks = list(map(int, data[index:index + n]))
    index += n
    
    edges = []
    for _ in range(n - 1):
        x = int(data[index])
        y = int(data[index + 1])
        edges.append((x, y))
        index += 2
    
    result = min_health_decrement(n, attacks, edges)
    results.append(result)

for result in results:
    print(result)
