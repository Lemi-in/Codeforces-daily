
n = 10
arr = [0] * n
updates = [[2,4,6],[5,6,8],[1,9,-4]]

for a in updates:
    s , e , inc = a[0] , a[1] , a[2]
    for i in range(s , e + 1):
        arr[i] += inc
print(arr)

# optimal
class Solution(object):
  def getModifiedArray(self, length, updates):
    """
    :type length: int
    :type updates: List[List[int]]
    :rtype: List[int]
    """
    ans = [0] * length
    for update in updates:
      start, end, delta = update
      ans[start] += delta
      if end + 1 < length:
        ans[end + 1] -= delta

    delta = 0
    for i in range(0, length):
      delta += ans[i]
      ans[i] = delta
    return ans
