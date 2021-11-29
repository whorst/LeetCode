def rotateMatrix(matrix):
    # Start by swapping (reversing) the rows in the array. Then iterate over the outside elements and swap them, starting at point 0,0.
    # Then go to the right of 0,0 and below 0,0. Swap those two points. Do that until you get to the end
    l = 0
    r = len(matrix) - 1
    while l < r:
        matrix[l], matrix[r] = matrix[r], matrix[l]
        l += 1
        r -= 1
    # transpose
    for row in matrix:
        print(row)
    for i in range(len(matrix)):
        for j in range(i):
            print("swapping ", matrix[i][j], "with ", matrix[j][i],"\n\n")
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            for row in matrix:
                print(row)
            print("\n")


matrix = [[1,2,3], [4, 5, 6], [7, 8, 9]]
rotateMatrix(matrix)
print(matrix)
