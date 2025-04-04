def min_length_after_operations(t, test_cases):
    results = []
    for s in test_cases:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  # Remove the last character if it matches the current one
            else:
                stack.append(char)  # Add the current character to the stack
        results.append(len(stack))  # The length of the stack is the minimum achievable length
    return results

# Input reading
t = int(input())
test_cases = [input().strip() for _ in range(t)]

# Solve and output results
results = min_length_after_operations(t, test_cases)
for res in results:
    print(res)


"""

Skibidus is given a string s
 that consists of lowercase Latin letters. If s
 contains more than 1
 letter, he can:

Choose an index i
 (1≤i≤|s|−1
, |s|
 denotes the current length of s
) such that si=si+1
. Replace si
 with any lowercase Latin letter of his choice. Remove si+1
 from the string.
Skibidus must determine the minimum possible length he can achieve through any number of operations.

Input
The first line contains an integer t
 (1≤t≤100
) — the number of test cases.

The only line of each test case contains a string s
 (1≤|s|≤100
). It is guaranteed s
 only contains lowercase Latin letters.

Output
For each test case, output an integer on the new line, the minimum achievable length of s
.

Example
InputCopy
4
baa
skibidus
cc
ohio
OutputCopy
1
8
1
4
Note
In the first test case, Skibidus can:

Perform an operation on i=2
. He replaces s2
 with b and removes s3
 from the string. Then, s
 becomes bb.
Perform an operation on i=1
. He replaces s1
 with b and removes s2
 from the string. Then, s
 becomes b.
Because s
 only contains 1
 letter, Skibidus cannot perform any more operations.
Therefore, the answer is 1
 for the first test case.

In the second test case, he cannot perform an operation on any index. Therefore, the answer is still the length of the initial string, 8
.

"""