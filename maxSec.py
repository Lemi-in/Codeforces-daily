def max_and_second_max_frequency(arr):
    freq_map = {}
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    max_freq = second_max_freq = float('-inf')

    for freq in freq_map.values():
        if freq > max_freq:
            second_max_freq = max_freq
            max_freq = freq
        elif freq > second_max_freq and freq != max_freq:
            second_max_freq = freq

    return max_freq, second_max_freq

# Example usage:
arr = [1, 2, 3, 2, 2, 1, 4, 4, 4, 4]
max_freq, second_max_freq = max_and_second_max_frequency(arr)
print("Max Frequency:", max_freq)
print("Second Max Frequency:", second_max_freq)

"""
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        container = {}
        total = 0
        l = 0
        r = 0
        
        while r < len(fruits):
            fruit = fruits[r]
            container[fruit] = r
            
            if len(container) > 2:
                minIn = min(container.values())
                del container[fruits[minIn]]
                l = minIn + 1
                
            total = max(total, r - l + 1)
            r += 1
        
        return total
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n ,m = len(s1) ,len(s2)
        if n > m:
            return False
        s1C, s2C = {},{}
        for i in range(n):
            s1C[s1[i]] = s1C.get(s1[i], 0) + 1
            s2C[s2[i]] = s2C.get(s2C[i], 0) + 1
        if pC == sC:
            return True
        else:
            return False
        j = 0
        for i in range(m,n):
            sC[s[i]] = sC.get(s[i], 0) + 1
            sC[s[j]] -= 1
            if sC[s[j]] == 0:
                sC.pop(s[j])
            j += 1
            if sC == s1C:
                return True
            else:
                return False
