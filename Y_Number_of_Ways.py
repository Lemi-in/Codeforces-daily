def count_ways(S, E):
    if S == E:
        return 1
    if S > E:
        return 0
    return count_ways(S + 1, E) + count_ways(S + 2, E) + count_ways(S + 3, E)

# Read input
S, E = map(int, input().split())

# Compute and print the result
print(count_ways(S, E))
