def ls(): return input().split()
def ints(): return map(int, input().split())
def strs():return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))


n ,k = ints()
a = li()
cnt = 0
num = a[k - 1]
for i in range(n):
    if a[i] >= num and a[i] > 0:
        cnt += 1
print(cnt)
