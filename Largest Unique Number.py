def find(arr):
    arr.sort(reverse=True)  # Sort in descending order
    n = len(arr)
    
    for i in range(n):

        if (i == 0 or arr[i] != arr[i - 1]) and (i == n - 1 or arr[i] != arr[i + 1]):
            return arr[i]
    
    return -1

# Example usage
nums1 = [5, 7, 3, 9, 4, 9, 8, 3, 1]
nums2 = [9, 9, 8, 8]
nums3 = [1, 2, 2, 3, 3, 4]
print(find(nums1))  # Output: 8
print(find(nums2))  # Output: -1
print(find(nums3))  # Output: 4
