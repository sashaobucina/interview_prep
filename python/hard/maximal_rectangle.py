from typing import List


def maximal_rectangle(matrix: List[List[int]]) -> int:
    """
    # 85: Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing 
    only 1's and return its area.

    This implementation uses monotonic stacks as the driver, using the technique derived by finding
    the maximal area rectangle in a histogram (# 84).
    """
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])

    def _construct(histogram: List[int], row: List[int]):
        for i in range(n):
            histogram[i] = 0 if row[i] == "0" else histogram[i] + 1

        return histogram

    max_area = 0
    histogram = [int(x) for x in matrix[0]]
    for i in range(m - 1):
        max_area = max(max_area, max_rect_in_histogram(histogram))
        histogram = _construct(histogram, matrix[i + 1])

    max_area = max(max_area, max_rect_in_histogram(histogram))

    return max_area


def max_rect_in_histogram(histogram: List[int]) -> int:
    """
    This runs in O(n) time.
    """
    max_area = 0
    in_stk = [-1]

    N = len(histogram)
    for i in range(N):
        while in_stk[-1] != -1 and histogram[in_stk[-1]] > histogram[i]:
            max_area = max(
                max_area, histogram[in_stk.pop()] * (i - in_stk[-1] - 1))

        in_stk.append(i)

    while in_stk[-1] != -1:
        max_area = max(
            max_area, histogram[in_stk.pop()] * (N - in_stk[-1] - 1))

    return max_area


if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    assert maximal_rectangle(matrix) == 6

    print("Passed all tests!")
