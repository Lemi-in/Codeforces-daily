
m, s = map(int, input().split())
if s == 0:
    if m == 1:
        print("0 0")
    else:
        print("-1 -1")
else:
    if s > 9 * m:
        print("-1 -1")
    else:
        mxx = [0] * m
        curr = s
        for i in range(m):
            if curr >= 9:
                mxx[i] = 9
                curr -= 9
            else:
                mxx[i] = curr
                curr = 0

        mnn = [0] * m
        curr = s - 1
        
        for i in range(m - 1, 0, -1):
            if curr >= 9:
                mnn[i] = 9
                curr -= 9
            else:
                mnn[i] = curr
                curr = 0
        mnn[0] = curr + 1

        print(''.join(map(str, mnn)) , ''.join(map(str, mxx)))
