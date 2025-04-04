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
	h, w = minp()

	mat = []
	for i in range(h):
		s = sinp()
		mat.append(s)

	side, up = [[0] * w for i in range(h)], [[0] * w for i in range(h)]

	for i in range(h):
		for j in range(w):
			if mat[i][j] == "." and j > 0 and mat[i][j-1] == ".":
				side[i][j] = 1
			if mat[i][j] == "." and i > 0 and mat[i-1][j] == ".":
				up[i][j] = 1

	# for r in side:
	# 	print(r)
	# print()
	# for r in up:
	# 	print(r)
	# print()

	for i in range(h):
		for j in range(w):
			if i > 0:
				side[i][j] += side[i-1][j]
				up[i][j] += up[i-1][j]
			if j > 0:
				side[i][j] += side[i][j-1]
				up[i][j] += up[i][j-1]
			if i > 0 and j > 0:
				side[i][j] -= side[i-1][j-1]
				up[i][j] -= up[i-1][j-1]

	q = iinp()
	for _ in range(q):
		r1, c1, r2, c2 = minp()
		r1 += 1
		curr = up[r2-1][c2-1]
		if c1 - 2 >= 0:
			curr -= up[r2-1][c1-2]
		if r1 - 2 >= 0:
			curr -= up[r1-2][c2-1]
		if r1-2 >= 0 and c1-2 >= 0:
			curr += up[r1-2][c1-2]


		r1 -= 1
		c1 += 1
		curr2 = side[r2-1][c2-1]
		if c1 - 2 >= 0:
			curr2 -= side[r2-1][c1-2]
		if r1 - 2 >= 0:
			curr2 -= side[r1-2][c2-1]
		if r1-2 >= 0 and c1-2 >= 0:
			curr2 += side[r1-2][c1-2]

		print(curr + curr2)



def main():
	t = 1
	# t = int(input())
	for i in range(t):
		solve()
	
if __name__ == "__main__":
	main()