#author: Lemi
import sys

def st(): return sys.stdin.readline().strip()

def backtrack(i, store, n, ans, s):
    if i == n:
        if store:
            ans.append("".join(store))  # Collect non-empty subsequences
        return
    
    # Include the current character
    store.append(s[i])
    backtrack(i + 1, store, n, ans, s)
    store.pop()
    
    # Exclude the current character
    backtrack(i + 1, store, n, ans, s)

def solve():
    s = st()
    n = len(s)
    ans = []
    
    backtrack(0, [], n, ans, s)
    ans.sort()  # Sort lexicographically
    
    for a in ans:
        print(a)

solve()