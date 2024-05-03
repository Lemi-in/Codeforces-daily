n, s = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 0
goodSegment = float('inf')  
currentSum = 0
while right < n:
    currentSum += a[right]
    while currentSum >= s:
        goodSegment = min(goodSegment, right - left + 1)
        currentSum -= a[left]
        left += 1
    right += 1

if goodSegment == float('inf'):
    print(-1)
else:
    print(goodSegment)



class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = maxKey = 0
        counts = {'T': 0, 'F': 0}

        for right in range(len(answerKey)):
            counts[answerKey[right]] += 1
            max_count = max(counts.values())
            
            while right - left + 1 - max_count > k:
                counts[answerKey[left]] -= 1
                left += 1

            maxKey = max(maxKey, right - left + 1)

        return maxKey
    
    
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        k = 1
        maxLen = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            maxLen = max(maxLen, right - left)
            
        return maxLen

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefSum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.prefSum[i] = self.prefSum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefSum[right + 1] - self.prefSum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


