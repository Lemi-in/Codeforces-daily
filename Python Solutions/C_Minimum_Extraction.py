def maximal_minimum(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        arr = test_cases[i][1]

        results.append(max(arr))

    return results

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

# Output
results = maximal_minimum(t, test_cases)
for result in results:
    print(result)
