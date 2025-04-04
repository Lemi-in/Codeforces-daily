
def solve():
    n = int(input())
    arr = []
    
    for _ in range(n):
        l, r = map(int, input().split())
        arr.append((l, r))
    
    def can_complete(k):
        curr_pos = 0  # Start at position 0
        for l, r in arr:
            # Find the farthest position we can reach within this segment
            max_reach = min(curr_pos + k, r)
            # If we can't reach the segment, return False
            if max_reach < l:
                return False
            # Update current position to the farthest valid position
            curr_pos = max(l, curr_pos)
        return True

    left, right = 0, 10**9
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if can_complete(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(ans)
for _ in range(int(input())):
    solve()

