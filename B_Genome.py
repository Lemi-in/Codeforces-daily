n = int(input())
s = input()

A = s.count('A')
G = s.count('G')
C = s.count('C')
T = s.count('T')

if n % 4 != 0 or A > n // 4 or G > n // 4 or C > n // 4 or T > n // 4:
    print("===")
    
else:
    n //= 4
    A = n - A
    G = n - G
    C = n - C
    T = n - T
    genome = []
    for char in s:
        if char == '?':
            if A > 0:
                genome.append('A')
                A -= 1
            elif G > 0:
                genome.append('G')
                G -= 1
            elif C > 0:
                genome.append('C')
                C -= 1
            elif T > 0:
                genome.append('T')
                T -= 1
        else:
            genome.append(char)

    print(''.join(genome))

