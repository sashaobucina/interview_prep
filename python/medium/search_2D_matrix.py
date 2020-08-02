from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    # 74: Write an efficient algorithm that searches for a value in an m x n matrix.

    This matrix has the following properties:
        - Integers in each row are sorted from left to right.
        - The first integer of each row is greater than the last integer of the previous row.
    """
    if not matrix or not matrix[0]:
        return False

    # binary search to find corresponding row where target may be
    lo, hi = 0, len(matrix) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2

        if target < matrix[mid][0]:
            hi = mid
        elif target > matrix[mid][-1]:
            lo = mid + 1
        else:
            lo = mid
            break

    # binary search on potential row
    row = matrix[lo]

    # binary search to find target in potential row
    lo, hi = 0, len(row) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2

        if row[mid] == target:
            return True

        if target < row[mid]:
            hi = mid
        else:
            lo = mid + 1

    return row[lo] == target


if __name__ == "__main__":
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]

    assert search_matrix(matrix, 3)
    assert search_matrix(matrix, 50)
    assert search_matrix(matrix, 16)
    assert not search_matrix(matrix, 0)
    assert not search_matrix(matrix, 55)
    assert not search_matrix(matrix, 22)
    assert not search_matrix(matrix, 25)

    print("Passed all tests!")
