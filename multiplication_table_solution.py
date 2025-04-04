def solve(n: int, m: int, k: int) -> int:
    """
    Solve the problem of finding k-th largest number in n×m multiplication table.
    
    For example, if n=2, m=3:
    The multiplication table looks like:
    1 2 3
    2 4 6
    
    The numbers in non-decreasing order are: 1, 2, 2, 3, 4, 6
    So if k=4, we return 3 (the 4th largest number)
    """
    def count_smaller(x: int) -> int:
        """
        Count how many numbers in the table are less than or equal to x.
        For each row i, we can count numbers ≤ x by taking min(x // i, m)
        """
        count = 0
        for i in range(1, n + 1):
            # In row i, numbers are: i, 2i, 3i, ..., mi
            # So numbers ≤ x are: min(x // i, m)
            count += min(x // i, m)
        return count
    
    # Binary search between 1 and n*m
    left, right = 1, n * m
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        count = count_smaller(mid)
        
        if count >= k:
            # If we have at least k numbers ≤ mid,
            # try to find a smaller number that still works
            answer = mid
            right = mid - 1
        else:
            # Need a larger number to get more numbers ≤ mid
            left = mid + 1
    
    return answer

def main():
    # Read input: n, m, k
    n, m, k = map(int, input().split())
    
    # Print the answer
    print(solve(n, m, k))

if __name__ == "__main__":
    main() 