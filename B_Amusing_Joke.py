from collections import Counter
men = input()
chris = input()
pile = input()
new = men + chris
mp = Counter(new)
mp2 = Counter(pile)
if mp == mp2:
    print("YES")
else:
    print("NO")