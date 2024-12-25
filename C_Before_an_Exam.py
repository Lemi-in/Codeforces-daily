d, sumTime = map(int, input().split())
minTime = []
maxTime = []
for _ in range(d):
    x, y = map(int, input().split())
    minTime.append(x)
    maxTime.append(y)

minTotal = sum(minTime)
maxTotal = sum(maxTime)

if sumTime < minTotal or sumTime > maxTotal:
    print("NO")
else:
    print("YES")
    schedule = minTime[:]
    extra_hours = sumTime - minTotal
    for i in range(d):
        available = maxTime[i] - minTime[i]
        add_hours = min(extra_hours, available)
        schedule[i] += add_hours
        extra_hours -= add_hours
        if extra_hours == 0:
            break
    print(" ".join(map(str, schedule)))
