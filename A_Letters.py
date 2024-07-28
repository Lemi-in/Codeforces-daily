n, m = map(int, input().split())
rooms = list(map(int, input().split()))
letters = list(map(int, input().split()))

p = [0] * (n + 1)
for i in range(n):
    p[i + 1] = p[i] + rooms[i]

for letter in letters:
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if p[mid] < letter:
            left = mid + 1
        else:
            right = mid
    dorm = left
    room = letter - p[left - 1]
    print(dorm, room)


    