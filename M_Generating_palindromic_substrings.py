def find_palindromes(s):
    n = len(s)
    palindromes = set()

    # Function to expand around center
    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1

    # Expand around each character (odd-length palindromes)
    for i in range(n):
        expand(i, i)       # Odd-length palindrome
        expand(i, i + 1)   # Even-length palindrome

    # Print lexicographically sorted palindromes
    for p in sorted(palindromes):
        print(p)

# Read input
s = input().strip()
find_palindromes(s)
