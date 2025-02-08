def find_kth(n, k):
    while n > 0:
        mid = 1 << (n - 1)  # 2^(n-1)
        if k == mid:
            return n  # Middle element is always `n`
        elif k < mid:
            n -= 1  # Search in the first half
        else:
            k -= mid  # Adjust `k` and search in the second half
            n -= 1

# Read input
n, k = map(int, input().split())
print(find_kth(n, k))








# power = 1
# for i in range(1, n):
#     power *= 2


# temp = (power + 1) // 2

# if k > temp:
#     k = power - k

# for i in range(n, 0, -1):
#     if k % (2 ** (i - 1)) == 0:
#         print(i)
#         break
