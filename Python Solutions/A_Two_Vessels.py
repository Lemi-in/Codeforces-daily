t = int(input()) 
for _ in range(t):
    a, b, c = map(int, input().split())  
    diff = abs(a - b)  
   
    if diff == 0:
        print(0)
    else:
      
        moves = (diff + c - 1) // c  
        print(moves)
