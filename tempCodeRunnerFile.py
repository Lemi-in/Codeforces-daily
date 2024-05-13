def longest_subarray_sum(arr):
    max_length = 0
    max_sum = 0
    current_length = 1
    current_sum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            current_length += 1
            current_sum += arr[i]
        else:
            if current_length > max_length:
                max_length = current_length
                max_sum = current_sum
            current_length = 1
            current_sum = arr[i]

    # Check if the last subarray is the longest
    if current_length > max_length:
        max_length = current_length
        max_sum = current_sum

    return max_sum

# Test case
arr = [3,5,3,1, 2, 3, 4, 5, 7, 0, 4, 0]
result = longest_subarray_sum(arr)
print("Sum of the longest subarray:", result)
