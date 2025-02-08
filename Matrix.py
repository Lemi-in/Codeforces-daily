class Matrix:
    # function to get all elemnents in each cell and their respectie elements in the other sides exact position
    def findSides(matrix, i, j):
        n, m = len(matrix), len(matrix[0])
        reflections = {
            "Top-Bottom": (n - 1 - i, j),
            "Left-Right": (i, m - 1 - j),
            "Main-Diagonal": (j, i),
            "Anti-Diagonal": (n - 1 - j, m - 1 - i)
        }
        reflected_values = {
            key: matrix[x][y] for key, (x, y) in reflections.items() if 0 <= x < n and 0 <= y < m
        }
        mat = mat[n - 1 - i][j] + mat[i][m - 1 - j] + mat[j][i] + mat[n - 1 - j][m - 1 - i]
        return reflected_values
    

    # a function to get the elements of the matrix in a spiral order
    def spiralOrder(matrix):
        if not matrix: return []

        m, n = len(matrix), len(matrix[0])
        left, right = 0, n - 1
        top, bottom = 0, m - 1
        ans = []

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
                
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans

    # a function to get each layer of a matrix 
    def Layers(matrix):
        n, m = len(matrix), len(matrix[0])  
        layers = []  
        
        top, left, bottom, right = 0, 0, n - 1, m - 1  
        
        while top <= bottom and left <= right:
            layer = []  
            for i in range(left, right + 1):
                layer.append(matrix[top][i])

            for i in range(top + 1, bottom + 1):
                layer.append(matrix[i][right])
            
            if top != bottom:
                for i in range(right - 1, left - 1, -1):
                    layer.append(matrix[bottom][i])
            
            if left != right:
                for i in range(bottom - 1, top, -1):
                    layer.append(matrix[i][left])
            
            layers.append(layer)  
            
            top += 1
            left += 1
            bottom -= 1
            right -= 1
        
        return layers
    
    # function to get the columns of a matrix
    def columns(matrix):
        if not matrix:
            return []
        
        num_cols = len(matrix[0])
        return [[row[i] for row in matrix] for i in range(num_cols)]
    # a function to get the columns of a matrix of different sized rows

    def get_columns(matrix):
        if not matrix:
            return []
        
        max_cols = max(len(row) for row in matrix)  # Find the longest row
        columns = [[] for _ in range(max_cols)]  # Create empty lists for columns

        for row in matrix:
            for i in range(len(row)):  # Only iterate over existing elements
                columns[i].append(row[i])

        return columns