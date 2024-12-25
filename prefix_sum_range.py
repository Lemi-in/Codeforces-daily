
def pref(arr, rangee, update):
   n = len(arr)
   diff = [0] * (n + 2)
   m = len(rangee)
   for j in range(m):
      l , r = rangee[j]
      diff[l] += update
      diff[r + 1] -= update
   print(diff)
   for i in range(1, n):
      diff[i] += diff[i - 1]
      arr[i] += diff[i]
   print(diff)

   return arr  

arr = [0,1,1,1,1,1]
rangee = [[1,3],[4,5],[3,4],[1,5]]
update = 10
print(pref(arr, rangee, update))