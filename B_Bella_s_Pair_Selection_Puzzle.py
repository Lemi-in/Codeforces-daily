# n, m = map(int, input().split())
# temp = [0] * 5
# for i in range(1, m + 1):
#     temp[i % 5] += 1
# ans = 0
# for i in range(1, n + 1):
#     ans += temp[(5 - i % 5) % 5]
# print(ans)
n, m = map(int, input().split())

temp = [0] * 5
i = 1
while i <= m:
    temp[i % 5] += 1
    i += 1

ans = 0
i = 1
while i <= n:
    ans += temp[(5 - i % 5) % 5]
    i += 1

print(ans)
