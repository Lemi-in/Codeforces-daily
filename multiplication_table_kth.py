def find_kth_largest(n: int, m: int, k: int) -> int:
    """
    Find the k-th largest number in an n×m multiplication table.
    
    Args:
        n: Number of rows
        m: Number of columns
        k: The k-th largest number to find
        
    Returns:
        The k-th largest number in the multiplication table
    """
    def count_numbers_less_equal(x: int) -> int:
        """
        Count how many numbers in the table are less than or equal to x.
        For each row i, we can count numbers ≤ x by taking min(x // i, m)
        """
        count = 0
        for i in range(1, n + 1):
            count += min(x // i, m)
        return count
    
    # Binary search between 1 and n*m (the largest possible number in the table)
    left, right = 1, n * m
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        count = count_numbers_less_equal(mid)
        
        if count >= k:
            # If we have at least k numbers less than or equal to mid,
            # try to find a smaller number that still satisfies this
            result = mid
            right = mid - 1
        else:
            # If we have less than k numbers, we need a larger number
            left = mid + 1
    
    return result

def main():
    # Read input
    n, m, k = map(int, input().split())
    
    # Find and print the result
    result = find_kth_largest(n, m, k)
    print(result)

if __name__ == "__main__":
    main() 