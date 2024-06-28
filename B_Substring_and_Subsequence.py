T = int(input())
for _ in range(T):
  a = input()
  b = input()
  ans = len(a) + len(b)
  for st in range(len(b)):
    ptr = st
    for i in range(len(a)):
      if ptr < len(b) and a[i] == b[ptr]:
        ptr += 1
    ans = min(ans, len(a) + len(b) - ptr + st)
  print(ans)