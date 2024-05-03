n = int(input())
s = str(n)

count4 = {}

for num in s:
    count4[num] = count4.get(num, 0) + 1

lucky = count4.get('4', 0) + count4.get('7', 0)
if lucky == 4 or lucky == 7:
    print("YES")
else:
    print("NO")