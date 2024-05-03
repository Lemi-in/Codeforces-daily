# Read input strings
s = input().strip()
t = input().strip()

# Initialize pointers and count of moves
i, j, moves = 0, 0, 0

# Iterate through both strings simultaneously
while i < len(s) and j < len(t):
    # If characters at current positions are equal, move to next positions
    if s[i] == t[j]:
        i += 1
        j += 1
    else:
        # If characters are not equal, increment moves and delete the leftmost character
        if len(s) > len(t):
            i += 1
        else:
            j += 1
        moves += 1

# Add remaining characters of longer string to moves
moves += max(len(s) - i, len(t) - j)

# Print the minimum number of moves required
print(moves)
