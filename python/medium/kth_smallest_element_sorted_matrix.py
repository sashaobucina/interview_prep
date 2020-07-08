from typing import List


def kth_smallest(matrix: List[List[int]], k: int) -> int:
    """
    # 378: Given a n x n matrix where each of the rows and columns are sorted in ascending order, 
    find the kth smallest element in the matrix.

    NOTE: It is the kth smallest element in the sorted order, not the kth distinct element.

    Time complexity: O(nlog(max_val))
    Space complexity: O(1)
    """
    n = len(matrix)
    lo, hi = matrix[0][0], matrix[n - 1][n - 1]

    while lo <= hi:
        mid = (lo + hi) // 2
        count = _count(matrix, n, mid)

        if count >= k:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo


def _count(matrix: List[List[int]], n: int, mid: int) -> int:
    count = 0
    row, col = n - 1, 0

    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            row -= 1
        else:
            count += row + 1
            col += 1

    return count


def kth_smallest_naive(matrix: List[List[int]], k: int) -> int:
    """
    Time complexity: O(n^2logn^2)
    Space complexity: O(n^2)
    """
    flattened = []
    for i in range(len(matrix)):
        flattened += matrix[i]

    flattened.sort()
    return flattened[k - 1]


if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    assert kth_smallest(matrix, 8) == kth_smallest_naive(matrix, 8) == 13

    print("Passed all tests!")
