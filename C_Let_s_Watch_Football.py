import math

def minimum_wait_time(a, b, c):
    t = math.ceil(c * (a - b) / b)
    return t

# Input reading
a, b, c = map(int, input().split())
print(minimum_wait_time(a, b, c))
