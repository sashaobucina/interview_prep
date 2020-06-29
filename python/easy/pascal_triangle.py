from typing import List


def pascalsTriangle(numRows: int) -> List[List[int]]:
    """
    # 118: Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
    """
    res = []
    for line in range(numRows):
        currRow = []
        for i in range(line + 1):
            currRow.append(_binomialCoeff(line, i))
        res.append(currRow)

    return res


def _binomialCoeff(n: int, k: int) -> int:
    res = 1
    if k > n - k:
        k = n - k

    for i in range(k):
        res = res * (n-i)
        res = res // (i+1)

    return res


def pascalsTriangleDP(numRows: int) -> List[List[int]]:
    """
    This sol'n uses dynamic programming.

    Time Complexity: O(numRows^2)
    """
    rows = []
    for i in range(numRows):
        row = [None] * (i + 1)
        row[0] = row[-1] = 1
        for j in range(1, i):
            row[j] = rows[i - 1][j] + rows[i - 1][j - 1]
        rows.append(row)

    return rows


if __name__ == "__main__":
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
                [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascalsTriangleDP(6) == pascalsTriangle(6) == expected

    print("Passed all tests!")
