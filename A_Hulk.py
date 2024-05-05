# Link: https://codeforces.com/problemset/problem/705/A
# Time complexity: O(n)
#I'm surprised that I solved It in the first try.
n = int(input())
hate = "I hate"
love = "I love"
it = "it"
that = "that"
space = " "
if n ==  1:
    print(hate + space + it)
    exit()
feeling = hate
for i in range(n - 1):
    feeling += space + that
    if i % 2 == 0:
        feeling += space + love
    else:
        feeling += space + hate
print(feeling + space + it )


