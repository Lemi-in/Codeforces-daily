# arr = [0,1, 2, 4]
# i = 0
# while (i < len(arr)):
#     correct = arr[i]
#     if (arr[i] < len(arr) and arr[i] != arr[correct]):
#         arr[i], arr[correct] = arr[correct], arr[i]
#     else:
#         i += 1
# print(arr)

# for i in range(1, len(arr)):
#     if arr[i] != i:
#         print(i)
# print(len(arr))

def cyclic_sort(nums):
    for cyclic_start in range(0, len(nums) - 1):
        item = nums[cyclic_start]
        pos = cyclic_start

        for i in range(cyclic_start + 1, len(nums)):
            if nums[i] < item:
                pos += 1
        if pos == cyclic_start:
            continue
        while item == nums[pos]:
            pos += 1
        nums[pos], item = item, nums[pos]
        
        while pos != cyclic_start:
            pos = cyclic_start
            for i in range(cyclic_start + 1, len(nums)):
                if nums[i] < item:
                    pos += 1
            while item == nums[pos]:
                pos += 1
            nums[pos], item = item, nums[pos]
    return nums

# Test cases
nums = [9, 60, 41, 2, 3, 5, 73, 0, 10, 5, 45, 75, 8, 633]
print(cyclic_sort(nums))
