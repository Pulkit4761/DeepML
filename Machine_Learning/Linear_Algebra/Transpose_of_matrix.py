'''Write a Python function that computes the transpose of a given matrix.'''

def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    if not a:
        return []

    rows = len(a)
    cols = len(a[0])

    b = [[0 for _ in range(rows)] for _ in range(cols)]

    # Fill the transposed matrix
    for i in range(rows):
        for j in range(cols):
            b[j][i] = a[i][j]

    return b