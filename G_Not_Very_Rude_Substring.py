# @date:2021-04-27 17:59:00
# @source:https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/G

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    c = int(data[1])
    s = data[2]
    
    l = 0
    ans = 0
    countA = 0
    countB = 0
    total= 0

    for r in range(n):
        if s[r] == 'a':
            countA += 1
        elif s[r] == 'b':
            countB += 1
            total += countA
        
        while total > c:
            if s[l] == 'a':
                total -= countB
                countA -= 1
            elif s[l] == 'b':
                countB -= 1
            l += 1
        
        ans = max(ans, r - l + 1)
    
    print(ans)

if __name__ == "__main__":
    main()
