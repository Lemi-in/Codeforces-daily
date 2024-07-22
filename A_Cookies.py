n = int(input())
a = list(map(int, input().split()))
cnt = 0
if n == 1:
    print(1)
    exit()
for num in a:
    if num % 2 != 0:
        cnt += 1
if cnt == 0:
    print(n)
    exit()
if cnt == n and n % 2 != 0:
    print(n)
    exit()
if cnt == n and n % 2 == 0:
    print(n - cnt)
    exit()

if cnt % 2 == 0:
    print(n - cnt)
else:
    print(cnt)

