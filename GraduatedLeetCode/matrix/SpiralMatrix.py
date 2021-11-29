def spiralOrder(matrix):
    res = []
    while matrix:
        # Extend will add all elements from matrix.pop(0) to res
        res = res + [x for x in matrix.pop(0)]

        # zip adds iterables together and puts them in a few tuples
        # * is like the spread operator
        print(matrix)
        all_matrix_elements = [*zip(*matrix)]
        # reverse matrix
        matrix = all_matrix_elements[::-1]
        print(matrix)
        print()
    return res


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
