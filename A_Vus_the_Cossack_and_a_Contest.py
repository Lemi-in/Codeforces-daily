def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

n , m, k = ints()

if m >= n and k >= n:
    print('Yes')
else:
    print('No')