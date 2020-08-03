from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    """
    # 64: Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right 
    which minimizes the sum of all numbers along its path.

    NOTE: You can only move either down or right at any point in time.
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[0][i] = grid[0][i] + dp[0][i - 1]
    for j in range(1, m):
        dp[j][0] = grid[j][0] + dp[j - 1][0]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    grid = []
    assert min_path_sum(grid) == 0

    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    assert min_path_sum(grid) == 7

    print("Passed all tests!")
