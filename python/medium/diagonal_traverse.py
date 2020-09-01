from typing import List
from collections import defaultdict


def find_diagonal_order(matrix: List[List[int]]) -> List[int]:
    """
    # 498: Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order.
    """
    if not matrix or not matrix[0]:
        return []

    ans = []
    R, C = len(matrix), len(matrix[0])

    up = True
    r, c = 0, 0
    while len(ans) < (R * C):
        if up:
            while r >= 0 and c < C:
                ans.append(matrix[r][c])
                c += 1
                r -= 1

            if c >= C:
                r += 2
                c -= 1
            else:
                r += 1

        else:
            while r < R and c >= 0:
                ans.append(matrix[r][c])
                c -= 1
                r += 1

            if r >= R:
                r -= 1
                c += 2
            else:
                c += 1

        up = not up

    return ans


def find_diagonal_order_intuitive(matrix: List[List[int]]) -> List[int]:
    """
    The key here is to realize that the sum of indices on all diagonals are equal.
    """
    d = defaultdict(list)
    R, C = len(matrix), len(matrix[0])
    for r in range(R):
        for c in range(C):
            d[r + c].append(matrix[r][c])

    ans = []
    for _sum in sorted(d):
        l = d[_sum]
        if _sum % 2 == 0:
            for x in l[::-1]:
                ans.append(x)
        else:
            for x in l:
                ans.append(x)

    return ans


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert find_diagonal_order(matrix) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
    assert find_diagonal_order_intuitive(matrix) == [1, 2, 4, 7, 5, 3, 6, 8, 9]

    print("Passed all tests!")
