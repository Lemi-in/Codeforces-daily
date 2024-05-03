n = int(input())

summ = 0
step = 0
while summ < n:
    if n >= 5 :
        summ += 5
        step += 1
    elif n >= 4:
        summ += 4
        step += 1
    elif n >= 3:
        summ += 3
        step += 1
    
    elif n >= 2:
        summ += 2
        step += 1
    elif n < 2:
        summ += 1
        step += 1
print(step)
