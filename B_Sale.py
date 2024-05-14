n , m = map(int, input().split())
a = list(map(int, input().split()))
negatives = [abs(i) for i in a if i < 0]
negatives = sorted(negatives, reverse=True)
profit = 0
j = 0
k = len(negatives)

while j < m and j < k:
    profit += negatives[j]
    j += 1
print(profit)