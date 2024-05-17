# Read the input values for a, b, and c
a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

# Calculate different possible results
ans = a + b + c
ans = max(ans, (a + b) * c)
ans = max(ans, a * (b + c))
ans = max(ans, a * b * c)

# Print the maximum result
print(ans)
