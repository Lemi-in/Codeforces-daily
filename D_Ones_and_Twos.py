t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    pos = set(i for i in range(n) if a[i] == 1)
    
    for _ in range(q):
        cmd = int(input())
        
        if cmd == 1:
            v = int(input())
            num = len(pos)
            
            if (v - num) % 2 == 1:
                if num == 0:
                    print("NO")
                else:
                    s1 = 2 * max(pos) - (num - 1)
                    s2 = 2 * (n - min(pos) - 1) - (num - 1)
                    print("YES" if v <= max(s1, s2) else "NO")
            else:
                print("YES" if v <= 2 * n - num else "NO")
        else:
            i, x = map(int, input().split())
            i -= 1
            pos.discard(i)
            a[i] = x
            if a[i] == 1:
                pos.add(i)
