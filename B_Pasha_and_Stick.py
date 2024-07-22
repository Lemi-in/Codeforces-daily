import math
n = int(input())
if n % 2 != 0:
    print(0)
elif n < 6:
    print(0)
else:
    print(math.ceil(n / 4) - 1)



# 6 = 1
# 8 = 1
# 10 = 2
# 12 = 2
# 14 = 3
# 16 = 3
# 18 = 4
# 20 = 4
# 22 = 5
# 24 = 5
# 26 = 6
# 28 = 6




