# Read input
s = input().strip()
n = len(s)

# If the string length is less than 26, it's impossible to form a nice substring
if n < 26:
    print(-1)
else:
    found = False
    
    # Sliding window to check each substring of length 26
    for i in range(n - 25):
        substring = s[i:i+26]
        count = [0] * 26
        question_marks = 0

        # Count the occurrences of each character and the number of question marks
        for char in substring:
            if char == '?':
                question_marks += 1
            else:
                count[ord(char) - ord('A')] += 1

        # Determine the missing characters
        missing_chars = [chr(j + ord('A')) for j in range(26) if count[j] == 0]

        # Check if we can replace the question marks with the missing characters
        if len(missing_chars) <= question_marks:
            idx = 0
            result = list(s)
            
            # Replace the question marks in the substring
            for j in range(26):
                if substring[j] == '?':
                    result[i + j] = missing_chars[idx]
                    idx += 1
                    if idx >= len(missing_chars):
                        break

            # Replace remaining question marks in the entire string with 'A'
            for j in range(n):
                if result[j] == '?':
                    result[j] = 'A'

            print(''.join(result))
            found = True
            break

    if not found:
        print(-1)
