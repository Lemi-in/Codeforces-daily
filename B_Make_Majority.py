
for _ in range(int(input().strip())):
    n = int(input())
    S = input()
    nums = []
    i = 0
    while i < len(S):
        if S[i] == '0':
            while i < len(S) and S[i] == '0':
                i += 1
            nums.append(0)
        else:
            nums.append(1)
            i += 1
    i , j = 0 , 0
    for num in nums:
        if num == 0:
            i += 1
        else:
            j += 1
    print("Yes" if j > i else "No")