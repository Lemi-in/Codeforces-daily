def process_queries(t, test_cases):
    results = []
    
    for case in test_cases:
        n, q = case['n'], case['q']
        arr = case['arr']
        queries = case['queries']
        
        # Precompute prefix and suffix sums
        prefix_sum = [0] * (n + 1)
        suffix_sum = [0] * (n + 2)
        
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
        
        for i in range(n, 0, -1):
            suffix_sum[i] = suffix_sum[i + 1] + arr[i - 1]
        
        # Process each query
        for l, r, k in queries:
            # Calculate the new sum after the modification
            prefix_part = prefix_sum[l - 1]  # Sum of elements before index l
            suffix_part = suffix_sum[r + 1]  # Sum of elements after index r
            modified_range_sum = (r - l + 1) * k  # The sum of the range [l, r] after modification
            
            total_sum = prefix_part + modified_range_sum + suffix_part
            
            # Check if the new sum is odd or even
            if total_sum % 2 == 1:
                results.append("YES")
            else:
                results.append("NO")
    
    return results


# Input Reading
t = int(input())  # Number of test cases
test_cases = []
for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    for _ in range(q):
        l, r, k = map(int, input().split())
        queries.append((l, r, k))
    test_cases.append({'n': n, 'q': q, 'arr': arr, 'queries': queries})

# Process the test cases
results = process_queries(t, test_cases)

# Output the results
for result in results:
    print(result)
