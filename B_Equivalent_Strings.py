def smallest(s):
    if len(s) % 2 == 1:
        return s
    s1 = smallest(s[:len(s) // 2])
    s2 = smallest(s[len(s) // 2:])
    return min(s1 + s2, s2 + s1)

s1 = input().strip()
s2 = input().strip()

print("YES" if smallest(s1) == smallest(s2) else "NO")
