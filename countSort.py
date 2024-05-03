
arr = [4, 2, 2, 8, 3, 3, 1]
max_value = max(arr)
    
    # Initialize a list to store counts of each element
counts = [0] * (max_value + 1)
    
    # Count the occurrences of each element
for num in arr:
    counts[num] += 1

print(counts)
sorted_arr = []

for i in range(len(counts)):
    sorted_arr.extend([i] * counts[i])

print(sorted_arr)