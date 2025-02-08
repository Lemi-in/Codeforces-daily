def ls(): return input().split()
def ints(): return map(int, input().split())
def strs():return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

for _ in range(it()):
    n = it()
    arr = []
    cnt = 0
    while n > 0:
        if n % 10 > 0:
            arr.append(n % 10 * (10 ** cnt))
        n //= 10
        cnt += 1
    print(len(arr))
    print(*arr)
        
