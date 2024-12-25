# def check(arr):
#     n = len(arr)
#     arr.sort()
#     for i in range(1, n):
#         if arr[i][0] < arr[i - 1][1]:
#             return False

#     return True

# intervals = [[0,30],[5,10],[15,20]]
# print(check(intervals))

def has_overlapping_intervals(intervals):
    max_time = max(end for _, end in intervals)
    diff = [0] * (max_time + 2)
    
    for start, end in intervals:
        diff[start] += 1
        diff[end + 1] -= 1
    
    active_intervals = 0
    for time in range(len(diff)):
        active_intervals += diff[time]
        if active_intervals > 1:
            return True
    
    return False

# Example usage
intervals = [[0, 30], [5, 10], [15, 20]]
print(has_overlapping_intervals(intervals))  
