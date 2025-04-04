def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  
            j -= 1
        arr[j + 1] = key  
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] 
    return arr
def counting_sort(arr):
    if not arr:
        return arr

    mx = max(arr)
    mn = min(arr)
    range_of_elements = mx - mn + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count[num - mn] += 1

    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - mn] - 1] = arr[i]
        count[arr[i] - mn] -= 1

    return output

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)



# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort:", bubble_sort(arr.copy()))
print("Insertion Sort:", insertion_sort(arr.copy()))
print("Selection Sort:", selection_sort(arr.copy()))

