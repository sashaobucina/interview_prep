from typing import List


def islandPerimeter(grid: list) -> int:
    """
    # 463: You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by 
    water, and there is exactly one island (i.e., one or more connected land cells).

    The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
    One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 

    Determine the perimeter of the island.
    """
    n, m = len(grid), len(grid[0])
    perimeter, edges = 0, 0

    perimeter = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                perimeter += 1
                edges += grid[i - 1][j] if i > 0 else 0
                edges += grid[i][j - 1] if j > 0 else 0

    return (4 * perimeter) - (2 * edges)


if __name__ == "__main__":
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    assert islandPerimeter(grid) == 16

    print("Passed all tests!")
