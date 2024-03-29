from typing import List


def rotate_image(matrix: List[List[int]]) -> None:
    """
    # 48: You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).

    NOTE: You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
    DO NOT allocate another 2D matrix and do the rotation.
    """
    n = len(matrix)

    # transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse horizontally
    for i in range(n):
        for j in range(0, n // 2):
            matrix[i][j], matrix[i][n - j - 1] = \
                matrix[i][n - j - 1], matrix[i][j]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    rotate_image(matrix)
    assert matrix == expected

    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    expected = [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]
    rotate_image(matrix)
    assert matrix == expected

    print("Passed all tests!")
