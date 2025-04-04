import sys

MOD = 1000000007

def mod_exponentiation(n, m, mod=MOD):
    if m == 0:
        return 1  # Base case: N^0 = 1
    half = mod_exponentiation(n, m // 2, mod)  # Compute (N^(M//2))
    half = (half * half) % mod  # Square it
    if m % 2 == 1:  # If M is odd, multiply by N once more
        half = (half * n) % mod
    return half

# Read input
n, m = map(int, sys.stdin.readline().split())

# Compute result
result = mod_exponentiation(n, m)

# Print output
sys.stdout.write(str(result) + "\n")
