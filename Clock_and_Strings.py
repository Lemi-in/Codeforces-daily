class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(A, B, C):
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)

def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the integers for the current test case
    a, b, c, d = map(int, input().split())

    # Create points for the segments
    A = Point(0, a)
    B = Point(0, b)
    C = Point(0, c)
    D = Point(0, d)

    # Check if the segments intersect and print the result
    if intersect(A, B, C, D):
        print("YES")
    else:
        print("NO")
