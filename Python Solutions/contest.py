a = [1, 1, 3, 3, 3, 5, 8, 8]
b = [1, 3, 3, 4, 5, 5, 5]

pairs = 0
i = j = 0

while i < len(a) and j < len(b):
    if a[i] == b[j]:
        count_a = 1
        count_b = 1
        
        # Count duplicates in a
        while i + 1 < len(a) and a[i] == a[i + 1]:
            count_a += 1
            i += 1
        
        # Count duplicates in b
        while j + 1 < len(b) and b[j] == b[j + 1]:
            count_b += 1
            j += 1
        
        pairs += count_a * count_b
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1

print(pairs)
