n = int(input())
num = 0
for _ in range(n):
    a = input() 
    if a == "X++" or a == "++X":
        num += 1
    else:
        num -= 1
print(num)