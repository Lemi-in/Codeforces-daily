
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    strings = [input().strip() for _ in range(n)]
    
    string_set = set(strings)
    print(string_set)
    
    for s in strings:
        found = False
        for j in range(1, len(s)):
            if s[:j] in string_set and s[j:] in string_set:
                found = True
                break
        if found:
            print('1', end='')
        else:
            print('0', end='')
    print()  
