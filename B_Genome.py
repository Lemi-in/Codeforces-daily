n = int(input())
s = input()

if n < 4 or n % 4 != 0:
    print("===")
    exit()

cntA = 0
cntG = 0
cntC = 0
cntT = 0
un = 0

for i in range(n):
    if s[i] == 'A':
        cntA += 1
    elif s[i] == 'G':
        cntG += 1
    elif s[i] == 'C':
        cntC += 1
    elif s[i] == 'T':
        cntT += 1
    else:
        un += 1
t = list(s)

for i in range(n):
    if t[i] == "?":
        if cntA < n // 4:
            t[i] = "A"
            cntA += 1
        elif cntG < n // 4:
            t[i] = "G"
            cntG += 1
        elif cntC < n // 4:
            t[i] = "C"
            cntC += 1
        elif cntT < n // 4:
            t[i] = "T"
            cntT += 1
m = "".join(t)
print(m)

