t = int(input())

def can_win(grid):
    n = len(grid[0])
    for j in range(n):
        # Determine the range of possible values in the j-th column after substitution
        max_val = max(grid[0][j], grid[1][j], grid[2][j])
        min_val = min(grid[0][j], grid[1][j], grid[2][j])
        
        # If the range doesn't cover 1, Alice cannot win
        if not (min_val <= 1 <= max_val):
            return False
    return True

for _ in range(t):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(3)]
    
    # Check if Alice can win
    if can_win(grid):
        print("YES")
    else:
        print("NO")
