# Read input
n = int(input().strip())
a = input().strip()

relation = {'0': '', '1': '', '2': '2', '3': '3', '4': '322', '5': '5', '6': '53', '7': '7', '8': '7222', '9': '7332'
}
arr = []
for digit in a:
    arr.append(relation[digit])
arr = ''.join(arr)
ans = sorted(arr, reverse=True)
print(''.join(ans))
