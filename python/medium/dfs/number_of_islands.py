"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""
def numberOfIslands(grid: list) -> int:
  if len(grid) == 0 or len(grid[0]) == 0:
    return 0

  n, m = len(grid), len(grid[0])
  visited = [[False for j in range(m)] for i in range(n)]

  count = 0
  for i in range(n):
    for j in range(m):
      if not visited[i][j] and grid[i][j] == 1:
        dfs(grid, i, j, visited)
        count += 1
  return count


def dfs(grid: list, i: int, j: int, visited: list) -> None:
  neighborRow, neighborCol = [1, 0, -1, 0], [0, 1, 0, -1]
  visited[i][j] = True

  for k in range(4):
    if isSafe(grid, i + neighborRow[k], j + neighborCol[k], visited):
      dfs(grid, i + neighborRow[k], j + neighborCol[k], visited)


def isSafe(grid: list, i: int, j: int, visited: list) -> bool:
  return (i >= 0 and i < len(grid) and
          j >= 0 and j < len(grid[0]) and
          not visited[i][j] and grid[i][j] == 1)



if __name__ == "__main__":
  grid = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
  print(numberOfIslands(grid))