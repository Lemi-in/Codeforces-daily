
mp = {}
for _ in range(int(input())):
    a , x = map(int, input().split())
    mp[a] = x
mp2 = {}
for _ in range(int(input())):
    b , y  = map(int, input().split())
    mp2[b] = y
sm = 0
for key in mp.keys():
    if key in mp2.keys():
        sm += max(mp[key], mp2[key])
    else:
        sm += mp[key]
for key in mp2.keys():
    if key not in mp.keys():
        sm += mp2[key]
    
print(sm)