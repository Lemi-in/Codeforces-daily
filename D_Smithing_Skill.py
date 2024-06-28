# Reading input
import sys
input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
m = int(data[index + 1])
index += 2

a = list(map(int, data[index:index + n]))
index += n
b = list(map(int, data[index:index + n]))
index += n
c = list(map(int, data[index:index + m]))

# Calculate the net consumption for each weapon class
net_consumption = [a[i] - b[i] for i in range(n)]

# Calculate the maximum experience points
total_experience = 0

for j in range(m):
    min_consumption = float('inf')
    
    # Find the weapon class with the minimum net consumption
    for i in range(n):
        if net_consumption[i] > 0:
            min_consumption = min(min_consumption, net_consumption[i])
    
    if min_consumption == float('inf'):
        continue
    
    # Calculate the maximum number of cycles for this type of metal
    cycles = c[j] // min_consumption
    
    # Each cycle gives 2 experience points
    total_experience += cycles * 2

print(total_experience)
