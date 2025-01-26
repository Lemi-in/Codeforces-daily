def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def i(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))


n , k = ints()
st = {i for i in range(k + 1)}
cnt = n
for _ in range(n):
    a = i()
    digits = set()
    while a > 0:
        digits.add(a % 10)
        a //= 10
    for s in st:
        if s not in digits:
            cnt -= 1
            break

print(cnt)