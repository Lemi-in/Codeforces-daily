def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

n = it()
t = s()
ans = ""
l , r = 0, 0
p , i = 0 , 0
while i < n:
    ans += t[i]
    p += 1
    i += (p)
print(ans)