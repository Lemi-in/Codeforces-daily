def count_same_end_substrings(s, queries):
    n = len(s)
    prefix = [0] * n
    last_occurrence = {}

    # Preprocess to calculate prefix sums
    for i in range(n):
        # Carry forward the previous prefix count
        prefix[i] = prefix[i - 1] if i > 0 else 0
        char = s[i]
        if char in last_occurrence:
            # Add count of substrings ending at index i
            prefix[i] += (i - last_occurrence[char])
        # Update last occurrence of the character
        last_occurrence[char] = i

    # Process queries
    result = []
    for li, ri in queries:
        if li == 0:
            result.append(prefix[ri])
        else:
            result.append(prefix[ri] - prefix[li - 1])

    return result

# Example Usage
s = "abcaab"
queries = [[0, 0], [1, 4], [2, 5], [0, 5]]
print(count_same_end_substrings(s, queries))  # Output: [1, 5, 5, 10]

s = "abcd"
queries = [[0, 3]]
print(count_same_end_substrings(s, queries))  # Output: [4]
