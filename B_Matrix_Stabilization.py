t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while True:
        found = False
        for i in range(n):
            for j in range(m):
                is_local_max = True
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] >= matrix[i][j]:
                        is_local_max = False
                        break
                if is_local_max:
                    matrix[i][j] -= 1
                    found = True
                    break
            if found:
                break
        if not found:
            break
    for row in matrix:
        print(' '.join(map(str, row)))