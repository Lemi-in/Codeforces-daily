import sys

def is_match(s, p, s_idx, p_idx, mapping, used_substrings):
    # Base case: both s and p are fully matched
    if s_idx == len(s) and p_idx == len(p):
        return True
    
    # If only one of them is exhausted, return False
    if s_idx == len(s) or p_idx == len(p):
        return False
    
    pattern_char = p[p_idx]
    
    # If the pattern character is already mapped
    if pattern_char in mapping:
        assigned_str = mapping[pattern_char]
        length = len(assigned_str)
        
        # Check if the mapped substring matches `s` from `s_idx`
        if s[s_idx:s_idx + length] == assigned_str:
            return is_match(s, p, s_idx + length, p_idx + 1, mapping, used_substrings)
        else:
            return False

    # If pattern character is not mapped, try all possible substrings
    for end in range(s_idx + 1, len(s) + 1):
        new_sub = s[s_idx:end]
        
        # Ensure that each substring is uniquely assigned
        if new_sub in used_substrings:
            continue
        
        # Assign the new substring and proceed
        mapping[pattern_char] = new_sub
        used_substrings.add(new_sub)
        
        if is_match(s, p, end, p_idx + 1, mapping, used_substrings):
            return True
        
        # Backtrack
        del mapping[pattern_char]
        used_substrings.remove(new_sub)

    return False

# Read input
t = int(sys.stdin.readline().strip())

for _ in range(t):
    s = sys.stdin.readline().strip()
    p = sys.stdin.readline().strip()
    
    if is_match(s, p, 0, 0, {}, set()):
        print("YES")
    else:
        print("NO")
