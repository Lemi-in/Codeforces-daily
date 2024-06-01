n = int(input())
a = list(map(int, input().split()))


a.sort(reverse=True)

max_len = 0  
current_max = a[0]  

for count in a:

    if count > current_max:
        count = current_max 
    max_len += count  
    current_max = max(count - 1, 0)  

print(max_len)
