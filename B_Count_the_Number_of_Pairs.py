for _ in range(int(input())):
    n, k = map(int, input().split())
    N = 26
    s = input()
    big = [0] * N
    small = [0] * N
    for i in s:
        if 'A' <= i <= 'Z':
            big[ord(i) - ord('A')] += 1
        else:
            small[ord(i) - ord('a')] += 1
    answer = 0
    for i in range(N):
        pairs = min(small[i], big[i])
        answer += pairs
        small[i] -= pairs
        big[i] -= pairs
        add = min(k, max(small[i], big[i]) // 2)
        k -= add
        answer += add
    print(answer)