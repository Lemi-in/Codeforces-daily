def dieter(cal, k , l , u):
    n = len(cal)
    left = 0
    sm = 0
    T = 0
    for right in range(n):
        sm += cal[right]
        if right - left + 1 > k:
            sm -= cal[left]
            left += 1
        if right - left + 1 == k:
            if sm > u:
                T += 1
            elif sm < l:
                T -= 1
    return T

calories = [6,5,0,0]
k = 2
lower = 1
upper = 5
print(dieter(calories, k , lower, upper))



