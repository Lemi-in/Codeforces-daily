k , n , w = map(int, input().split())
total = 0
for i in range(1,w + 1):
    price = k
    price *= i
    total += price
if total < n:
    print(0)
    exit()
borrow = total - n
print(borrow)