import sys

def compute_contributions(arr, n, is_min=True):
    """ Computes the sum of min or max contributions over all subarrays. """
    stack = []
    left = [0] * n
    right = [0] * n
    result = 0

    # Calculate left boundary (how far each element can extend to the left)
    for i in range(n):
        while stack and (arr[stack[-1]] > arr[i] if is_min else arr[stack[-1]] < arr[i]):
            stack.pop()
        left[i] = i - stack[-1] if stack else i + 1
        stack.append(i)

    stack.clear()

    # Calculate right boundary (how far each element can extend to the right)
    for i in range(n - 1, -1, -1):
        while stack and (arr[stack[-1]] >= arr[i] if is_min else arr[stack[-1]] <= arr[i]):
            stack.pop()
        right[i] = stack[-1] - i if stack else n - i
        stack.append(i)

    # Compute contribution to sum
    for i in range(n):
        result += arr[i] * left[i] * right[i]

    return result

def imbalance_value(n, arr):
    max_contrib = compute_contributions(arr, n, is_min=False)
    min_contrib = compute_contributions(arr, n, is_min=True)
    return max_contrib - min_contrib

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    print(imbalance_value(n, arr))
