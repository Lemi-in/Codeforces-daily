t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    big = [0] * 26
    small = [0] * 26

    for i in s:
        if 'A' <= i <= 'Z':
            big[ord(i) - ord('A')] += 1
        else:
            small[ord(i) - ord('a')] += 1

    answer = 0
    for i in range(26):
        pairs = min(small[i], big[i])
        answer += pairs
        small[i] -= pairs
        big[i] -= pairs
        add = min(k, max(small[i], big[i]) // 2)
        k -= add
        answer += add

    print(answer)