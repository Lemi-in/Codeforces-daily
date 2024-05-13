
n = int(input())
matrix = [input() for _ in range(n)]

diagonalChar = matrix[0][0] 
NonDiagonalChar = matrix[0][1]

if diagonalChar == NonDiagonalChar:
    print("NO")
    exit()

for i in range(n):
    for j in range(n):
        if i == j:
            if matrix[i][j] != diagonalChar:
                print("NO")
                exit()
        elif i + 1 == n - j:
            if matrix[i][j] != diagonalChar:
                print("NO")
                exit()
        elif matrix[i][j] != NonDiagonalChar:
            print("NO")
            exit()
print("YES")















n = int(input())
matrix = [input() for _ in range(n)]

diagonaSet = set()  
NonDiagonaSet = set()

for i in range(n):
    for j in range(n):
        if i == j or i + 1 == n - j:  
            diagonaSet.add(matrix[i][j])
        else:
            NonDiagonaSet.add(matrix[i][j])

if len(diagonaSet) == 1 and len(NonDiagonaSet) == 1 and diagonaSet != NonDiagonaSet:
    print("YES")
else:
    print("NO")
