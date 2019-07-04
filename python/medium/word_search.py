"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of a sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighbouring. The same 
letter cell cannot be used more than once.
"""
def wordSearch(grid: list, word: str) -> bool:
  # TODO
  # NOTE: Potentially try a DP or memoization solution while keeping a visited set of indices.
  # Initial base case
  if not grid or len(grid) == 0 or len(grid[0]) == 0:
    return False

  m, n = len(grid), len(grid[0])
  res = False
  for i in range(m):
    for j in range(n):
      if dfs(grid, word, i, j, 0):
        return True
  return res

def dfs(grid: list, word: str, i: int, j: int, k: int) -> bool:
  if grid[i][j] != word[k]:
    return False

  if k >= len(word) - 1:
    return True

  d_i = [-1, 0, 1, 0]
  d_j = [0, 1, 0, -1]
  char = grid[i][j]
  grid[i][j] = '#'

  # TODO
  for m in range(4):
    p_i = i + d_i[m]
    p_j = j + d_j[m]
    if p_i >= 0 and p_i < len(grid) and p_j >= 0 and p_j < len(grid[0]) \
                and grid[p_i][p_j] == word[k + 1]:
      if dfs(grid, word, p_i, p_j, k + 1):
        return True

  grid[i][j] = char
  return False

if __name__ == "__main__":
  matrix = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
  ]
  print(wordSearch(matrix, "ABCCED"))   # True
  matrix = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
  ]
  print(wordSearch(matrix, "SEE"))   # True
  matrix = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
  ]
  print(wordSearch(matrix, "ABCB"))   # False