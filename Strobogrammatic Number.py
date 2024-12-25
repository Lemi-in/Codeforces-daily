def check(num):
    s = {"0","1","6","8","9"}
    n = len(num)
    l , r = 0, n - 1

    while l < r:
        if num[l] not in s or num[r] not in s:
            return False
        
        if (num[l] == num[r] and (num[l] in s and num[r] in s)) or (num[l] == "6" and num[r] == "9") or (num[l] == "9" and num[r] == "6"):
            l += 1
            r -= 1
        else:
            return False
    return True

num = "9988"

print(check(num))

