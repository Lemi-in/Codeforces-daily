t = int(input())
for _ in range(t):
    n, c = map(str, input().split())
    n = int(n)
    string = input()

    ans = 0
    start = -1
    for end in range(2 * n):
        if string[end % n] == c and start == -1:
            start = end
        if start != -1 and string[end % n] == 'g':
            ans = max(ans, end - start)
            start = -1
    print(ans)