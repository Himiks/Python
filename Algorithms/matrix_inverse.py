def rotate(mat):
    n = len(mat)
    res = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            res[n - j - 1][i] = mat[i][j]
            for row in res:
                print(" ".join(map(str, row)))
            print("")
            
    for i in range(n):
        for j in range(n):
            mat[i][j] = res[i][j]
    
    
mat = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

rotate(mat)