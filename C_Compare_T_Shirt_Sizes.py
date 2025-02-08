def ls(): return input().split()
def ints(): return map(int, input().split())
def strs(): return map(str, input().split())
def it(): return int(input())
def s(): return input()
def li(): return list(map(int, input().split()))

for _ in range(it()):
    a, b = strs()
    if a == b:
        print("=")
        continue
    
    if a == "M":
        print(">" if b[-1] == "S" else "<")
        continue
    if b == "M":
        print("<" if a[-1] == "S" else ">")
        continue

    if a[-1] == 'S' and b[-1] == 'S':
        print("<" if len(a) > len(b) else ">")
        continue
    
    if a[-1] == 'L' and b[-1] == 'L':
        print(">" if len(a) > len(b) else "<")
        continue

    print("<" if a[-1] == "S" else ">")
