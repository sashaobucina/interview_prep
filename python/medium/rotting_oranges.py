from typing import List
from collections import deque


def oranges_rotting(grid: List[List[int]]) -> int:
    """
    # 994: In a given grid, each cell can have one of three values:
        - the value 0 representing an empty cell;
        - the value 1 representing a fresh orange;
        - the value 2 representing a rotten orange.

    Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
    If this is impossible, return -1 instead.
    """
    m, n = len(grid), len(grid[0])

    good = set()
    bad = set()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                good.add((i, j))
            elif grid[i][j] == 2:
                bad.add((i, j))

    if not good:
        return 0

    # staging for BFS
    q = deque([])
    visited = set()

    for i, j in bad:
        q.appendleft((i, j, 0))
        visited.add((i, j))

    # perform BFS, due to properties of BFS minutes are guaranteed to smallest for each encountered fresh apple
    res = 0
    while q:
        x, y, minutes = q.pop()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x2, y2 = x + dx, y + dy

            if 0 <= x2 < m and 0 <= y2 < n and (x2, y2) not in visited and grid[x2][y2] == 1:
                q.appendleft((x2, y2, minutes + 1))

                res = max(res, minutes + 1)
                visited.add((x2, y2))
                good.discard((x2, y2))

    return res if not good else -1


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert oranges_rotting(grid) == 4

    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert oranges_rotting(grid) == -1

    grid = [[0, 2]]
    assert oranges_rotting(grid) == 0

    print("Passed all tests!")
