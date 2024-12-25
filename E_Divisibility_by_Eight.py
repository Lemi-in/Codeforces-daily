n = input().strip()
size = len(n)

for i in range(size):
    if int(n[i]) % 8 == 0:
        print("YES\n", n[i], sep="")
        exit()
    for j in range(i + 1, size):
        if int(n[i] + n[j]) % 8 == 0:
            print("YES\n", n[i] + n[j], sep="")
            exit()
        for k in range(j + 1, size):
            if int(n[i] + n[j] + n[k]) % 8 == 0:
                print("YES\n", n[i] + n[j] + n[k], sep="")
                exit()

print("NO")
