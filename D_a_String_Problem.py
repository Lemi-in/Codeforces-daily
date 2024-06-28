def compute_prefix_function(s):
    n = len(s)
    pi = [0] * n
    j = 0
    
    for i in range(1, n):
        while (j > 0 and s[i] != s[j]):
            j = pi[j - 1]
        
        if s[i] == s[j]:
            j += 1
        else:
            j = 0
        
        pi[i] = j
    
    return pi

t = int(input().strip())
results = []

for _ in range(t):
    s = input().strip()
    n = len(s)
    
    # Compute prefix function for string s
    pi = compute_prefix_function(s)
    
    # Set to store all valid substrings t
    valid_substrings = set()
    
    # Adding the full string s itself if not all 'a'
    if s != 'a' * n:
        valid_substrings.add(s)
    
    # Adding all substrings defined by the prefix function
    for i in range(1, n):
        if pi[i] > 0:
            valid_substrings.add(s[:pi[i]])
    
    results.append(len(valid_substrings))

# Print all results
for result in results:
    print(result)
