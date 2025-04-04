import sys, math
from functools import cmp_to_key
from operator import itemgetter
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque

input = sys.stdin.readline

def iinp(): return (int(input()))
def linp(): return (list(map(int, input().split())))
def sinp(): return (input().strip())
def minp(): return (map(int, input().split()))

def solve():
	n = iinp()

	queries = []
	arr = set()
	for i in range(n):
		l, r = minp()
		queries.append((l, r))
		arr.add(l)
		arr.add(r + 1)

	arr = sorted(list(arr))
	mp = {}
	m = len(arr)
	for i in range(m):
		mp[arr[i]] = i

	pf = [0] * (m)
	for l, r in queries:
		pf[mp[l]] += 1
		pf[mp[r + 1]] -= 1
	for i in range(1, m):
		pf[i] += pf[i-1]

	ans = [0] * (n + 1)
	for i in range(1, m):
		ans[pf[i-1]] += arr[i] - arr[i-1]
	print(*ans[1:])

def main():
	t = 1
	# t = int(input())
	for i in range(t):
		solve()
	
if __name__ == "__main__":
	main()