import sys

def kth_symbol(n, k):
    if n == 1:
        return 0
    mid = 2**(n-2)  # Midpoint of the row
    if k <= mid:
        return kth_symbol(n-1, k)  # Same as first half
    else:
        return 1 - kth_symbol(n-1, k-mid)  # Flipped version of (K-mid)

# Read input
input = sys.stdin.read
data = input().split("\n")
T = int(data[0])

# Process test cases
result = []
for i in range(1, T+1):
    if data[i].strip():
        N, K = map(int, data[i].split())
        result.append(str(kth_symbol(N, K)))

# Print all results efficiently
sys.stdout.write("\n".join(result) + "\n")
