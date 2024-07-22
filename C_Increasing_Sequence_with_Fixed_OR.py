for _ in range(int(input())):
    n = int(input())
    bits = [1 << i for i in range(61) if n & (1 << i)]
    seq = [n] + [n - b for b in bits if n - b > 0]
    seq.reverse()
    print(len(seq))
    print(' '.join(map(str, seq)))