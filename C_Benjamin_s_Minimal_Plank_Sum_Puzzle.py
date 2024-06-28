n , k = map(int, input().split())
arr = list(map(int, input().split()))
l , r = 0 , 0
summ = float("inf")
win = []

while r < n:
    summ += arr[l]
    win.append(arr[l]):
    