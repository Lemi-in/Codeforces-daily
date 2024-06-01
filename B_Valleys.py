t = int(input())
for _ in range(t):
  
  n = int(input())
  arr = list(map(int,input().split()))
  

  result = 'YES'
  count = 0
  for i in range(n-1):
    if arr[i]<arr[i+1]:
      count=1
    elif arr[i]>arr[i+1] and count==1:
      result = 'NO'
      break
  print(result)
