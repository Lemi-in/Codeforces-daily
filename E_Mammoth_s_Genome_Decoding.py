n = int(input())
s = input()

# Count the occurrences of each nucleotide and '?'
count = {'A': 0, 'C': 0, 'G': 0, 'T': 0, '?': 0}
for char in s:
    count[char] += 1

# Calculate the target count for each nucleotide
target_count = n // 4

# Check if it's possible to decode the genome
if count['A'] > target_count or count['C'] > target_count or count['G'] > target_count or count['T'] > target_count:
    print("===")
else:
    # Replace '?' with the missing nucleotides
    decoded_genome = ''
    for char in s:
        if char == '?':
            if count['A'] < target_count and count['?'] >= target_count - count['A']:
                decoded_genome += 'A'
                count['A'] += 1
            elif count['C'] < target_count and count['?'] >= target_count - count['C']:
                decoded_genome += 'C'
                count['C'] += 1
            elif count['G'] < target_count and count['?'] >= target_count - count['G']:
                decoded_genome += 'G'
                count['G'] += 1
            elif count['T'] < target_count and count['?'] >= target_count - count['T']:
                decoded_genome += 'T'
                count['T'] += 1
        else:
            decoded_genome += char
    
    # Check if the counts are now equal for all nucleotides
    if count['A'] == count['C'] == count['G'] == count['T'] == target_count:
        print(decoded_genome)
    else:
        print("===")