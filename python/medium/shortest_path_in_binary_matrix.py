from collections import deque

"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of 
cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
  - C_1 is at location (0, 0) (ie. has value grid[0][0])
  - C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
  - If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).

Return the length of the shortest such clear path from top-left to bottom-right. 
If such a path does not exist, return -1.
"""
def shortest_path(grid: list) -> int:
  if not grid or len(grid) == 0:
    return -1

  n = len(grid)
  q = deque([(0, 0, 1)])
  while len(q) > 0:
    x, y, distance = q.popleft()

    if x == n - 1 and y == n - 1:
      return distance

    for i, j in ((x-1,y+1), (x-1,y), (x-1,y-1), (x,y-1), (x+1,y-1), (x+1,y), (x+1,y+1), (x,y+1)):
      if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
        q.append((i, j, distance + 1))
        grid[i][j] = 1

  return -1

if __name__ == "__main__":
  grid = [[0,0,0],[1,1,0],[1,1,0]]
  print(shortest_path(grid))    # expected: 4