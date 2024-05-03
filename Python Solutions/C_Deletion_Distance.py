s = str(input())
t = str(input())

pointerS = len(s) - 1
pointerT = len(t) - 1


equal = 0

while pointerS >= 0 and pointerT >= 0 and s[pointerS] == t[pointerT]:
    equal += 1
    pointerS -= 1
    pointerT -= 1

union = equal * 2

whole = len(s) + len(t)

moves = whole - union

print(moves)

