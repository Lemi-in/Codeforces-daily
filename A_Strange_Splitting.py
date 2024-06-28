
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     array = list(map(int, input().split()))
    
#     unique_elements = set(array)
#     if len(unique_elements) <= 1:
#         print("NO")
#     else:
#         print("YES")
#         coloring = ['R'] * n
#         coloring[1] = 'B'
#         print(''.join(coloring))

# Read the number of test cases
t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
   
    all_same = True
    for i in range(1, n):
        if array[i] != array[i-1]:
            all_same = False
            break
    
    if all_same:
        print("NO")
    else:
        print("YES")
        coloring = ['R'] * n
        coloring[1] = 'B'
        print(''.join(coloring))
