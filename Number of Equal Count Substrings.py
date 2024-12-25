from collections import Counter

def equal_count_substrings(s: str, count: int) -> int:
    n = len(s)
    result = 0
    
    for unique_chars in range(1, 27):  # Check for 1 to 26 unique characters
        freq = Counter()
        start = 0
        current_unique_count = 0
        
        for end in range(n):
            char_end = s[end]
            freq[char_end] += 1
            
            # Update current unique count
            if freq[char_end] == count:
                current_unique_count += 1
            elif freq[char_end] == count + 1:
                current_unique_count -= 1
            
            # While we have more unique characters than we want, contract the window
            while len(freq) > unique_chars:
                char_start = s[start]
                if freq[char_start] == count:
                    current_unique_count -= 1
                freq[char_start] -= 1
                if freq[char_start] == 0:
                    del freq[char_start]
                elif freq[char_start] == count:
                    current_unique_count += 1
                start += 1
            
            # Check if we have the exact number of unique characters and they all appear exactly `count` times
            if len(freq) == unique_chars and current_unique_count == unique_chars:
                result += 1
    
    return result

# Example usage:
print(equal_count_substrings("aaabcbbcc", 3))  # Output: 3
print(equal_count_substrings("abcd", 2))        # Output: 0
print(equal_count_substrings("a", 5))           # Output: 0