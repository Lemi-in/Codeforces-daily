t = int(input())

for _ in range(t):
  l, r = map(int, input().split())
  max_factors = 0

  for num in range(l, r + 1):
    factors = 0
    j = 2
    while j * j <= num:
      if num % j == 0:
        factors += 1
        num //= j
      else:
        j += 1
    if num > 1:
      factors += 1
    max_factors = max(max_factors, factors)

  print(max_factors)
