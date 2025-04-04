def min_time_to_display(q, test_cases):
    results = []
    for s, t in test_cases:
        n, m = len(s), len(t)
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(n + 1):
            for j in range(m + 1):
                # Append to the first screen
                if i < n:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
                # Append to the second screen
                if j < m:
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
                # Copy from the first screen to the second screen
                if i > 0 and i <= m and s[:i] == t[:i]:
                    dp[i][i] = min(dp[i][i], dp[i][j] + 1)
                # Copy from the second screen to the first screen
                if j > 0 and j <= n and t[:j] == s[:j]:
                    dp[j][j] = min(dp[j][j], dp[i][j] + 1)

        results.append(dp[n][m])
    return results


# Input reading and output
q = int(input())
test_cases = [tuple(input().strip() for _ in range(2)) for _ in range(q)]
results = min_time_to_display(q, test_cases)
print("\n".join(map(str, results)))


# Timur likes his name. As a spelling of his name, he allows any permutation of the letters of the name. For example, the following strings are valid spellings of his name: Timur, miurT, Trumi, mriTu. Note that the correct spelling must have uppercased T and lowercased other letters.

# Today he wrote string s
#  of length n
#  consisting only of uppercase or lowercase Latin letters. He asks you to check if s
#  is the correct spelling of his name.

# Input
# The first line of the input contains an integer t
#  (1≤t≤103
# ) — the number of test cases.

# The first line of each test case contains an integer n
#  (1≤n≤10)
#  — the length of string s
# .

# The second line of each test case contains a string s
#  consisting of only uppercase or lowercase Latin characters.

# Output
# For each test case, output "YES" (without quotes) if s
#  satisfies the condition, and "NO" (without quotes) otherwise.

# You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

# Example
# InputCopy
# 10
# 5
# Timur
# 5
# miurT
# 5
# Trumi
# 5
# mriTu
# 5
# timur
# 4
# Timr
# 6
# Timuur
# 10
# codeforces
# 10
# TimurTimur
# 5
# TIMUR
# OutputCopy
# YES
# YES
# YES
# YES
# NO
# NO
# NO
# NO
# NO
# NO

