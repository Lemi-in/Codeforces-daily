import sys
from collections import defaultdict

def solve():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    
    freq = defaultdict(int)
    count = 0
    
    for i in range(n):
        diff = a[i] - i
        count += freq[diff]
        freq[diff] += 1
    
    print(count)

t = int(sys.stdin.readline().strip())

for _ in range(t):
    solve()
