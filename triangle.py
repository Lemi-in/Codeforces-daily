def check(matrix, i, j):
    n, m = len(matrix), len(matrix[0])
    reflections = {
        "Top-Bottom": (n - 1 - i, j),
        "Left-Right": (i, m - 1 - j),
        "Main-Diagonal": (j, i),
        "Anti-Diagonal": (n - 1 - j, m - 1 - i)
    }
    
    reflected_values = {
        key: matrix[x][y] for key, (x, y) in reflections.items() if 0 <= x < n and 0 <= y < m
    }
    
    return reflected_values

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
i, j = 1, 0  # Middle element (5)
print(check(matrix, i, j))
