
mp = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h',
    9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
    16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v',
    23: 'w', 24: 'x', 25: 'y', 26: 'z'
}

for i in range(int(input())):
    n = int(input())
    s = input()
    s = s[::-1]
    ans = ""
    i = 0 
    while i < n :
        if s[i] == '0' :
            tmp = s[i + 1] + s[i + 2]
            tmp = tmp[::-1]
            ans += mp[int(tmp)]
            i += 3
        else:
            ans += mp[int(s[i])]
            i += 1
    print(ans[::-1])

