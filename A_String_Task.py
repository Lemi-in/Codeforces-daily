ss = input()
n = len(ss)
vowels = 'aeiouAEIOUYy'
t = ""
for s in ss:
    if s not in vowels:
        t += '.' + s.lower()
print(t)
