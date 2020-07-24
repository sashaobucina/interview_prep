from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """
    # 200: Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    visited = set()

    def dfs(x: int, y: int) -> None:
        visited.add((x, y))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < m and 0 <= y2 < n and grid[x2][y2] == "1" and (x2, y2) not in visited:
                dfs(x2, y2)

    islands = 0
    for i in range(m):
        for j in range(n):
            if not (i, j) in visited and grid[i][j] == "1":
                dfs(i, j)
                islands += 1

    return islands


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert num_islands(grid) == 1

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert num_islands(grid) == 3

    print("Passed all tests!")
