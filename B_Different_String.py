def rearrange_string(s):
    # Check if all characters are the same
    if len(set(s)) == 1:
        return "NO"

    # Rearrange the string by sorting it
    rearranged = ''.join(sorted(s))

    # Check if the rearranged string is the same as the original string
    if rearranged == s:
        return "NO"
    else:
        return "YES\n" + rearranged

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the string for the current test case
    s = input()

    # Rearrange the string and print the result
    print(rearrange_string(s))
