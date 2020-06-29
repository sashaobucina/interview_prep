def unique_path(m: int, n: int) -> int:
    """
    # 62: A robot is located at the top-left corner of a m x n grid.

    The robot can only move either down or right at any point in time. 
    The robot is trying to reach the bottom-right corner of the grid.

    How many possible unique paths are there?
    """
    def helper(x: int, y: int) -> int:
        if x == m - 1 and y == n - 1:
            return 1

        rightPath = helper(x + 1, y) if x + 1 < m else 0
        downPath = helper(x, y + 1) if y + 1 < n else 0
        return rightPath + downPath

    if m >= 0 and n >= 0:
        return helper(0, 0)
    return 0


def unique_path_dp(m: int, n: int) -> int:
    """
    This sol'n uses the recurrence relation T[i][j] = T[i-1][j] + T[i][j-1]

    Time complexity: O(n^2)
    Space complexity: O(n^2)
    """
    table = [[0 for y in range(n)] for x in range(m)]

    for i in range(m):
        table[i][0] = 1

    for j in range(n):
        table[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table[m - 1][n - 1]


if __name__ == "__main__":
    assert unique_path(3, 2) == 3
    assert unique_path_dp(3, 2) == 3
    assert unique_path_dp(23, 12) == 193536720

    print("Passed all tests!")
