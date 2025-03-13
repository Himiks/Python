def rotate(mat):
    n = len(mat)
    for row in mat:
        row.reverse()

    for row in mat:
        print(" ".join(map(str, row)))
    print("")

    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        for row in mat:
            print(" ".join(map(str, row)))
        print("")



mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

rotate(mat)

    # Print the rotated matrix
