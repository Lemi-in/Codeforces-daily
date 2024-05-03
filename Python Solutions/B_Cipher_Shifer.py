t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    left, right = 0 , 1
    result = ""
    while right < n:
        result += s[left]
        while right < n and s[left] != s[right]:
            right += 1
        left = right + 1
        right = left + 1
    print(result)





