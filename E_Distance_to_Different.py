MOD = 998244353


def count_possible_arrays(n, k):
  """
  This function calculates the number of possible arrays 'b' for given constraints.

  Args:
      n: The length of the array 'a'.
      k: The number of unique integers in 'a' (from 1 to k).

  Returns:
      The number of possible arrays 'b' modulo MOD.
  """
  # Initialize dp (dynamic programming) table to store counts for different sizes
  dp = [[0] * (k + 1) for _ in range(n + 1)]

  # Base case: No elements (empty array)
  dp[0][0] = 1

  # Iterate for each array size (1 to n)
  for i in range(1, n + 1):
    # Iterate for each possible unique integer (1 to k) at the current position
    for j in range(1, k + 1):
      # Count ways to form 'b' with current element 'j'
      count = 0

      # Case 1: Previous element is the same (distance to next different element)
      if i > 1 and dp[i - 1][j]:
        count += (dp[i - 1][j] * (i - 1)) % MOD

      # Case 2: Previous element is different (distance to previous different element + 1)
      for prev in range(1, k + 1):
        if prev != j and dp[i - 1][prev]:
          count += (dp[i - 1][prev] * (i - dp[i - 1][prev])) % MOD

      # Update dp table with the total count for the current position and element
      dp[i][j] = count % MOD

  # Sum the counts for all possible unique integers at the last position (n)
  total_count = 0
  for j in range(1, k + 1):
    total_count = (total_count + dp[n][j]) % MOD

  return total_count

if __name__ == "__main__":
  n, k = map(int, input().split())
  num_possible_arrays = count_possible_arrays(n, k)
  print(num_possible_arrays)
