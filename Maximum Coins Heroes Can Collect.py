def binary (arr, hero):
    l , r = 0 , len(arr) - 1
    idx = 0
    
    while l <= r:
        mid = (l + r) // 2
        if hero >= arr[mid][0]:
            idx = mid
            l = mid + 1
        else:
            r = mid - 1
    return idx


def maxCoins(h , m , c):
    mx = 0
    arr = []  
    res = []

    for i in range(len(m)):
        arr.append([monsters[i], coins[i]])  
    arr.sort(key=lambda x: x[0])

    pref = [0] * (len(arr) + 1)   
    for i in range(len(arr)):
        pref[i] = pref[i - 1] + arr[i][1]


    for hero in h:  
        ind = binary(arr, hero)
        res.append(pref[ind])
    
    return res

heroes = [5]
monsters = [2,3,1,2]
coins = [10,6,5,2]


print(maxCoins(heroes, monsters, coins))
