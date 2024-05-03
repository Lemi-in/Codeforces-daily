
nums1 = [1,2,3,0,0,0]
nums2 =[2,5,6]
nums3 = [] 
for num in nums1:
    if num != 0:
        nums3.append(num)  
for nums in nums2:
    if nums != 0:
        nums3.append(nums)  

nums1 = nums3
nums1.sort()

print(nums1)