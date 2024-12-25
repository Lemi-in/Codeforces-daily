def solve(t, test_cases):
    results = []

    for n in test_cases:
        s = list("BAN" * n)
        swaps = []

        # Calculate positions of A's
        A_positions = [i for i in range(len(s)) if s[i] == 'A']
        next_A_pos = len(s) - 1

        # Move each 'A' to the end by swapping
        for pos in reversed(A_positions):
            if pos < next_A_pos:
                swaps.append((pos + 1, next_A_pos + 1))
                s[pos], s[next_A_pos] = s[next_A_pos], s[pos]
                next_A_pos -= 1

        results.append((len(swaps), swaps))

    for result in results:
        print(result[0])
        for swap in result[1]:
            print(swap[0], swap[1])

# Input and call the solve function
t = int(input())
test_cases = [int(input()) for _ in range(t)]
solve(t, test_cases)
