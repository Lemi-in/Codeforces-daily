n, m = map(int, input().split())

songs = []
for _ in range(n):
    a, b = map(int, input().split())
    songs.append((a, b))

songs.sort(key=lambda x: x[1])  # Sort songs in non-decreasing order of bi

total_size = 0
count = 0
for song in songs:
    total_size += song[0]
    if total_size > m:
        break
    count += 1

if total_size > m:
    print("-1")
else:
    print(count)