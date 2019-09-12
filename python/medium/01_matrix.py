import sys
from collections import deque

max_int = sys.maxsize

"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""
def update_matrix(matrix: list) -> list:
  if len(matrix) == 0:
    return matrix

  row, col = len(matrix), len(matrix[0])

  dist = [[max_int for j in range(col)] for i in range(row)]
  q = deque([])
  for i in range(row):
    for j in range(col):
      if matrix[i][j] == 0:
        dist[i][j] = 0
        q.appendleft((i, j))

  directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
  while len(q) > 0:
    x, y = q.pop()
    for d in range(4):
      adj_x, adj_y = x + directions[d][0], y + directions[d][1]
      if adj_x >= 0 and adj_x < row and adj_y >= 0 and adj_y < col:
        if dist[adj_x][adj_y] > dist[x][y] + 1:
          dist[adj_x][adj_y] = dist[x][y] + 1
          q.appendleft((adj_x, adj_y))

  return dist

def update_matrix_dp(matrix: list) -> list:
  if len(matrix) == 0:
    return matrix

  row, col = len(matrix), len(matrix[0])
  dist = [[max_int for j in range(col)] for i in range(row)]

  # first pass: top to bottom, left to right
  for i in range(row):
    for j in range(col):
      if matrix[i][j] == 0:
        dist[i][j] = 0
      else:
        if i > 0:
          dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
        if j > 0:
          dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)

  # second pass: bottom to top, right to left
  for i in range(row - 1, -1, -1):
    for j in range(col - 1, -1, -1):
      if i < row - 1:
        dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
      if j < col - 1:
        dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)



  return dist



if __name__ == "__main__":
  matrix = [[0,0,0],
            [0,1,0],
            [1,1,1]]
  print(update_matrix(matrix))
    # expected:  [[0,0,0],
    #             [0,1,0],
    #             [1,2,1]]
  print(update_matrix_dp(matrix))