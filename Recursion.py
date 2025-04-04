class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n, k):
            if n == 1:
                return '0'
            
            length = (1 << n) - 1 
            mid = length // 2 + 1  
            
            if k == mid:
                return '1'
            elif k < mid:
                return helper(n - 1, k)
            else:
                return '1' if helper(n - 1, length - k + 1) == '0' else '0'
        
        return helper(n, k)

def generate_subsets(nums, index=0, subset=[]):
    if index == len(nums):
        print(subset)  # Print or store the subset
        return
    
    # Exclude the current element
    generate_subsets(nums, index + 1, subset)
    
    # Include the current element
    generate_subsets(nums, index + 1, subset + [nums[index]])

# Example Usage
generate_subsets([1, 2, 3])


def generate_permutations(nums, index=0):
    if index == len(nums):
        print(nums)  # Print or store the permutation
        return
    
    for i in range(index, len(nums)):
        nums[i], nums[index] = nums[index], nums[i]  # Swap
        generate_permutations(nums, index + 1)
        nums[i], nums[index] = nums[index], nums[i]  # Backtrack

# Example Usage
generate_permutations([1, 2, 3])



def tower_of_hanoi(n, src, aux, dest):
    if n == 1:
        print(f"Move disk 1 from {src} to {dest}")
        return
    
    tower_of_hanoi(n - 1, src, dest, aux)  # Move n-1 disks to auxiliary
    print(f"Move disk {n} from {src} to {dest}")  # Move nth disk to destination
    tower_of_hanoi(n - 1, aux, src, dest)  # Move n-1 disks to destination

# Example Usage
tower_of_hanoi(3, 'A', 'B', 'C')



def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(n, row=0, board=[]):
    if row == n:
        print(board)  # Print or store the board configuration
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            solve_n_queens(n, row + 1, board + [col])

# Example Usage
solve_n_queens(4)




def count_ways(n):
    if n == 0 or n == 1:
        return 1  # Base cases

    return count_ways(n - 1) + count_ways(n - 2)  # Take 1 step or 2 steps

# Example Usage
print(count_ways(5))  # Output: 8




def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example Usage
arr = [3, 1, 4, 1, 5, 9]
print(merge_sort(arr))  # Output: Sorted array




def kth_grammar(n, k):
    if n == 1:
        return 0
    
    mid = (1 << (n - 1)) // 2
    if k <= mid:
        return kth_grammar(n - 1, k)
    else:
        return 1 - kth_grammar(n - 1, k - mid)

# Example Usage
print(kth_grammar(4, 5))  # Output: 1




def count_partitions(n, m):
    if n == 0:
        return 1
    if n < 0 or m == 0:
        return 0
    return count_partitions(n - m, m) + count_partitions(n, m - 1)

# Example Usage
print(count_partitions(5, 5))  # Output: Number of ways




def ncr(n, r):
    if r == 0 or r == n:
        return 1
    return ncr(n - 1, r - 1) + ncr(n - 1, r)

# Read input
n, r = map(int, input().split())

# Compute and print the result
print(ncr(n, r))



def count_ways(S, E):
    if S == E:
        return 1
    if S > E:
        return 0
    return count_ways(S + 1, E) + count_ways(S + 2, E) + count_ways(S + 3, E)

# Read input
S, E = map(int, input().split())

# Compute and print the result
print(count_ways(S, E))


def find_subsequences(idx, current, current_sum, N, M, A, results):
    if current_sum == M:
        results.append(tuple(current))  # Store as a tuple to avoid duplicate lists
        return

    if idx >= N or current_sum > M:
        return

    # Include the current element
    find_subsequences(idx + 1, current + [A[idx]], current_sum + A[idx], N, M, A, results)

    # Skip all duplicates of A[idx]
    while idx + 1 < N and A[idx] == A[idx + 1]:
        idx += 1

    # Exclude the current element
    find_subsequences(idx + 1, current, current_sum, N, M, A, results)

def process_test_case(N, M, A):
    A.sort()  # Sort to maintain lexicographic order
    results = []
    find_subsequences(0, [], 0, N, M, A, results)

    if results:
        for seq in sorted(results):  # Sort to ensure proper lexicographic order
            print(" ".join(map(str, seq)))
    else:
        print("NONE")

    print()  # Blank line after each test case

# Reading input
T = int(input().strip())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    process_test_case(N, M, A)




def find_palindromes(s):
    n = len(s)
    palindromes = set()

    # Function to expand around center
    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1

    # Expand around each character (odd-length palindromes)
    for i in range(n):
        expand(i, i)       # Odd-length palindrome
        expand(i, i + 1)   # Even-length palindrome

    # Print lexicographically sorted palindromes
    for p in sorted(palindromes):
        print(p)

# Read input
s = input().strip()
find_palindromes(s)

