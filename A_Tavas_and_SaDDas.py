n = input()
l = len(n)
lucky = 2**l - 2
for indx, dig in enumerate(reversed(n)):
    if dig == '7':
        lucky += 2**indx
print(lucky + 1)