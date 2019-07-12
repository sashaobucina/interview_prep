"""
Same problem as unique_paths.py , however there are obstacles which are denoted as '1' in the grid, 
otherwise it is free, denoted by '0'.
"""
def uniquePathII(grid: list) -> int:
  m, n = len(grid), len(grid[0])

  # If starting cell has an obstacle, then there are no possible paths
  if grid[0][0] == 1:
    return 0

  # Number of ways to reach the starting cell
  grid[0][0] = 1

  # Filling in the values for the first column
  for i in range(1, m):
    grid[i][0] = int(grid[i][0] == 0 and grid[i - 1][0] == 1)

  # Filling in the values for the first row
  for j in range(1, n):
    grid[0][j] = int(grid[0][j] == 0 and grid[0][j - 1] == 1)

  # Starting from cell (1, 1), No. of ways to reach cell[i][j] = cell[i-1][j] + cell[i][j-1]
  for i in range(1, m):
    for j in range(1, n):
      if grid[i][j] == 0:
        grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
      else:
        grid[i][j] = 0

  # Return the value from the rightmost bottommost cell. That is the destination.
  return grid[m-1][n-1]

if __name__ == "__main__":
  obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
  print(uniquePathII(obstacleGrid))   # Expected value: 2