from typing import List


def set_zeros(matrix: List[List[int]]) -> None:
    """
    # 73: Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    row, col = False, False
    if matrix[0][0] == 0:
        row = True
        col = True
    else:
        if 0 in matrix[0]:
            row = True
        if any(matrix[i][0] == 0 for i in range(m)):
            col = True

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    if row:
        for i in range(n):
            matrix[0][i] = 0
    if col:
        for i in range(m):
            matrix[i][0] = 0


if __name__ == "__main__":
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeros(matrix)
    expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    assert matrix == expected

    print("Passed all tests!")
