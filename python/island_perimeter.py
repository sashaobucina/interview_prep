"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by 
water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.
"""
def islandPerimeter(grid: list) -> int:
  n, m = len(grid), len(grid[0])

  perimeter = 0
  for row in range(n):
    for col in range(m):
      if grid[row][col] == 1:
        perimeter += numAdjacentIslandBlocks(grid, [row, col])

  return perimeter

def numAdjacentIslandBlocks(grid: list, coord: list) -> int:
  count = 4
  row, col = coord
  directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  for dir in directions:
    dx, dy = dir
    if 0 <= row + dx < len(grid) and 0 <= col + dy < len(grid[0]):
      count -= grid[row + dx][col + dy]

  return count

if __name__ == "__main__":
  grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
  print(islandPerimeter(grid))  # expected: 16