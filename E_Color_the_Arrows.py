def solve_max_rewards(t, test_cases):
    results = []
    for n, s, c in test_cases:
        dp = c[:]  # dp[i] = max reward ending at i

        # Forward pass for '>'
        for i in range(n - 1):
            if s[i] == '>':
                if dp[i + 1] < dp[i] + c[i + 1]:
                    dp[i + 1] = dp[i] + c[i + 1]

        # Backward pass for '<'
        for i in range(n - 1, 0, -1):
            if s[i] == '<':
                if dp[i - 1] < dp[i] + c[i - 1]:
                    dp[i - 1] = dp[i] + c[i - 1]

        results.append(max(0, max(dp)))  # max reward or 0 if none
    return results


# Sample input
t = 5
test_cases = [
    (3, "<>>", [5, 4, 6]),
    (5, "<><>>", [5, -2, 4, -3, 7]),
    (2, ">>", [-1, -2]),
    (8, ">>>><<<<", [1, -1, 1, -1, 1, -1, 1, -1]),
    (5, "><<<>", [-1, 100, 100, 100, 100])
]

# Run and print result
for res in solve_max_rewards(t, test_cases):
    print(res)
