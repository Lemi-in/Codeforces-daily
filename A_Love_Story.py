def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def st(): return input()
def li(): return list(map(int, input().split()))

for _ in range(it()):
    s = st()
    code = "codeforces"
    cnt = 0
    for i in range(len(s)):
        if s[i] != code[i]:
            cnt += 1
    print(cnt)