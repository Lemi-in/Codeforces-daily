n = int(input())

magnets = []
for _ in range(n):
    m = input()
    magnets.append(m)
count = 1
for i in range(n - 1):
    if magnets[i] != magnets[i + 1]:
        count += 1
print(count)

    
    
