from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    count = Counter(s)
    if count['T'] != 2 * count['M']:
        print("NO")
        continue
    
    t_count = 0
    m_count = 0
    
    for char in s:
        if char == 'T':
            t_count += 1
        elif char == 'M':
            m_count += 1
        if m_count > t_count:
            print("NO")
            break
    else:
        t_count = 0
        m_count = 0
        for char in reversed(s):
            if char == 'T':
                t_count += 1
            elif char == 'M':
                m_count += 1
            if m_count > t_count:
                print("NO")
                break
        else:
            print("YES")
