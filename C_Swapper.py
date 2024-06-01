# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    s = input().strip()

    # Initialize counts for "AB" pairs and remaining characters
    ab_pairs = s.count("AB")
    remaining_chars = len(s) - (ab_pairs * 2)

    # Adjust the count based on remaining characters and "BA" pairs
    if ab_pairs > 0:
        valid_swaps = ab_pairs + remaining_chars
    else:
        valid_swaps = 0

    # Print the count of valid swaps for the current test case
    print(valid_swaps)
