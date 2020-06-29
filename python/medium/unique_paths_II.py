from typing import List


def unique_paths_II(grid: List[List[int]]) -> int:
    """
    # 63: A robot is located at the top-left corner of a m x n grid.

    The robot can only move either down or right at any point in time.
    The robot is trying to reach the bottom-right corner of the grid.

    Now consider if some obstacles are added to the grids. How many unique paths would there be?

    Recurrence relation: T[i][j] = T[i-1][j] + T[i][j-1].
    """
    m, n = len(grid), len(grid[0])

    if grid[0][0] == 1:
        return 0

    grid[0][0] = 1

    for i in range(1, m):
        grid[i][0] = int(grid[i][0] == 0 and grid[i - 1][0] == 1)

    for j in range(1, n):
        grid[0][j] = int(grid[0][j] == 0 and grid[0][j - 1] == 1)

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i - 1][j] + \
                grid[i][j - 1] if grid[i][j] == 0 else 0

    return grid[m-1][n-1]


if __name__ == "__main__":
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert unique_paths_II(grid) == 2

    print("Passed all tests!")
