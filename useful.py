#Created by timur_jalgasbaev
#Do'nt use this tamplate, please!!!!!!!
#I'm joking)))
#Place to find an idea to problem:
import sys
input=lambda:sys.stdin.readline().rstrip("\r\n")
from collections import defaultdict,deque
from itertools import permutations,combinations,product
from math import lcm,gcd,ceil
mod=int(1e9)+7
def fact(n):
    f=[0]*(n+1)
    f[0]=1
    for i in range(1,n+1):
        f[i]=f[i-1]*i%mod
inf=10**18
def arr():
    return list(map(int,input().split()))
def mtx(n,q):
    a=[]
    if q==0:
        for i in range(n):
            a.append(list(map(int,input().split())))
    if q==1:
        for i in range(n):
            a.append(input().split())
    if q==2:
        for i in range(n):
            a.append(list(input()))
    return a
def pf(a,n):
    pref=[0]*(n+1)
    for i in range(1,n+1):
        pref[i]=pref[i-1]+a[i-1]
    return pref
def prime(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n%2==0:
        return 0
    for i in range(3,n,2):
        if n%i==0:
            return 0
    return 1
def inv(n):
    return pow(n,mod-2,mod)
def comb_m(n,k):
    if n<k:
        return 0
    elif k<0:
        return 0
    return F[n]*inv(F(k)*F(n-k))%mod
def var(x,y,n):
    if 0<=x<n and 0<=y<n:
        return 1
    return 0
def eratos(n):
    prime=[1]*(n+1)
    prime[0]=0
    prime[1]=0
    p=2
    while (p*p<=n):
        if (prime[p]):
            for i in range(p*p,n+1,p):
                prime[i]=0
        p+=1
    return prime
def summ(n):
    r=0
    while n:
        r+=n%10
        n//=10
    return r
def lb(arr,d):
    left,right=0,len(arr)
    while left<right:
        mid=(left+right)//2
        if arr[mid]<d:
            left=mid+1
        else:
            right=mid
    return left
#F=fact(2*10**5)
#prime=eratos(2*10**5)
def solve():
    n=int(input())
    a=arr()
    b=arr()
    c=[]
    for i in range(n):
        c+=[a[i]-b[i]]
    c.sort()
    ans=0
    for i in range(n):
        if c[i]<=0:
            continue
        p=lb(c,-c[i]+1)
        ans+=i-p
    print(ans)
    
t=1
#t=int(input())
for i in range(t):
    solve()

def prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

def prefix(matrix):
    rows, cols = len(matrix), len(matrix[0])

    prefix = [row[:] for row in matrix]  

    for i in range(1, rows):  
        for j in range(cols):  
            prefix[i][j] += prefix[i-1][j] 

    return prefix
