# Reading input
n = int(input())
heights = list(map(int, input().split()))

mini = heights[0]
miniIndex = 0
maxi = heights[0]
maxiIndex = 0
# To handle the case where there are multiple max or min values
# we need to loop through the entire array
# and find the first and last index of the max and min values
# and then calculate the number of steps needed to move the
# tallest soldier to the rightmost position and the shortest
# soldier to the leftmost position

for i in range(1, n):
    if heights[i] > maxi:
        maxi = heights[i]
        maxiIndex = i
    if heights[i] <= mini:
        mini = heights[i]
        miniIndex = i

# If the tallest soldier is to the right of the shortest soldier
# then we need to move the tallest soldier to the rightmost position
# and the shortest soldier to the leftmost position
if maxiIndex > miniIndex:
    steps = maxiIndex + n - miniIndex - 2
else:
    steps = maxiIndex + n - miniIndex - 1

print(steps)