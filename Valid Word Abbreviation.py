def validate(s, a):
    n, m = len(s), len(a)
    i, j = 0, 0
    
    while i < n and j < m:
        if s[i] == a[j]:
            i += 1
            j += 1
        elif a[j].isdigit():
            k = 0
            while j < m and a[j].isdigit():
                k = k * 10 + int(a[j])
                j += 1
            i += k
        else:
            return False


    return i == n and j == m

word = "internationalization"
abbr = "i12iz4n"

print(validate(word, abbr))  #
