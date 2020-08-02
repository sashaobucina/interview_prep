from typing import List


def max_area_of_island(grid: List[List[int]]) -> int:
    """
    # 695: Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
    connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are 
    surrounded by water.

    Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
    """
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(x: int, y: int) -> int:
        grid[x][y] = 0

        area = 1
        for dx, dy in directions:
            x2, y2 = x + dx, y + dy
            if (0 <= x2 < m) and (0 <= y2 < n) and (grid[x2][y2] == 1):
                area += dfs(x2, y2)

        return area

    max_area = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area


if __name__ == "__main__":
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    assert max_area_of_island(grid) == 6

    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    assert max_area_of_island(grid) == 0

    print("Passed all tests!")
