def setZeroes(self, matrix) -> None:
    row_to_visit = set()
    column_to_visit = set()
    row_i = 0
    for row in matrix:
        column_i = 0
        for column in row:
            if matrix[row_i][column_i] == 0:
                row_to_visit.add(row_i)
                column_to_visit.add(column_i)
            column_i += 1
        if row_i in row_to_visit:
            matrix[row_i] = [0] * len(row)
        row_i += 1

    for column_i in column_to_visit:
        row_i = 0
        for row in matrix:
            matrix[row_i][column_i] = 0
            row_i += 1
    print(matrix)
    """
    Do not return anything, modify matrix in-place instead.
    """
