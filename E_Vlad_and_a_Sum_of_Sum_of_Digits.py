n = 200000
ans = [0] * (n + 1)
def digit(num):
    sm = 0
    while num > 0:
        sm += num % 10
        num //= 10
    return sm
for i in range(1 , n + 1):
    ans[i] = ans[i - 1] + digit(i)


for _ in range(int(input())):
    n = int(input())
    print(ans[n])