t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Initialize counters for triple occurrences
    triple_counts = {}
    beautiful_pairs = 0
    
    # Iterate through the array to count triple occurrences
    for i in range(n - 2):
        # Forming triples based on the current position
        triple1 = (a[i], a[i+1], a[i+2])
        triple2 = (a[i-1], a[i], a[i+1]) if i >= 1 else None
        triple3 = (a[i-2], a[i-1], a[i]) if i >= 2 else None
        
        # Update triple counts
        triple_counts[triple1] = triple_counts.get(triple1, 0) + 1
        if triple2:
            triple_counts[triple2] = triple_counts.get(triple2, 0) + 1
        if triple3:
            triple_counts[triple3] = triple_counts.get(triple3, 0) + 1
    
    # Iterate through the triple counts to calculate beautiful pairs
    for count in triple_counts.values():
        # For each occurrence count, calculate beautiful pairs
        beautiful_pairs += count * (count - 1) // 2
    
    print(beautiful_pairs)
