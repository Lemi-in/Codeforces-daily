#author: Lemi
import sys

def dfs(n):
    if n == 0:
        return 0
    
    cur, length = 1, 1
    while cur <= n:
        cur = cur * 10 + 1
        length += 1
    
    prev = cur // 10
    A = dfs(n % prev) + (n // prev) * (length - 1)
    B = dfs((cur - n) % prev) + length + (cur - n) // prev * (length - 1)
    
    return min(A, B)

def main():
    n = int(sys.stdin.readline().strip())
    res = dfs(n)
    print(res)

if __name__ == "__main__":
    main()
