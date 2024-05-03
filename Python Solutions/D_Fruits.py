# Read input
n, m = map(int, input().split())
prices = list(map(int, input().split()))

prices.sort()


fruit_freq = {}
for _ in range(m):
    fruit = input()
    fruit_freq[fruit] = fruit_freq.get(fruit, 0) + 1


sorted_fruits = sorted(fruit_freq.items(), key=lambda x: x[1], reverse=True)


min_price = sum(prices[i] * sorted_fruits[i][1] for i in range(len(sorted_fruits)))

max_price = sum(prices[-i-1] * sorted_fruits[i][1] for i in range(len(sorted_fruits)))

print(min_price, max_price)
