t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(input())
    b = list(input())
    a.sort(reverse=True)
    b.sort(reverse=True)
 
    consA = 0  
    consB = 0  
    result = ""
 
    while a and b:
        nextFromB = b[-1] < a[-1]  
        
        if nextFromB and consB == k:  
            nextFromB = False  
        
        if not nextFromB and consA == k:  
            nextFromB = True  
 
        if nextFromB:  
            result += b[-1] 
            consB += 1 
            consA = 0  
            b.pop()  
        else:
            result += a[-1]  
            consA += 1  
            consB = 0  
            a.pop() 
    
    print(result)
