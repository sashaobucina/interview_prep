from typing import List


def transpose(A: List[List[int]]) -> List[List[int]]:
    """
    # 867: Given a matrix A, return the transpose of A.

    The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column 
    indices of the matrix.
    """
    R, C = len(A), len(A[0])
    return [[A[i][j] for i in range(R)] for j in range(C)]


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert transpose(A) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    A = [[1, 2, 3], [4, 5, 6]]
    assert transpose(A) == [[1, 4], [2, 5], [3, 6]]

    print("Passed all tests!")
