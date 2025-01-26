from collections import Counter
def valid(n, m, s, cards):
    cnt = Counter(cards)
    left = 0
    v = 0
    win = Counter()

    for right in range(n):
        win[s[right]] += 1

        while win[s[right]] > cnt[s[right]]:
            win[s[left]] -= 1
            if win[s[left]] == 0:
                del win[s[left]]
            left += 1

        v += (right - left + 1)

    return v

n, m = map(int, input().split())
s = input()
cards = input()

print(valid(n, m, s, cards))
