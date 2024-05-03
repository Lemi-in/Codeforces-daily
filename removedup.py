prices = [7,6,4,3,1]
n = len(prices)
left , right = 0, 1
totalProfit = 0
while right < n:
    if prices[left] < prices[right]:
        profit = prices[right] - prices[left]
        totalProfit += profit
    left += 1
    right += 1
print( totalProfit)
        