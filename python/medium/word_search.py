"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of a sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighbouring. The same 
letter cell cannot be used more than once.
"""
def wordSearch(grid: list, word: str) -> bool:
  # TODO
  # NOTE: Potentially try a DP or memoization solution while keeping a visited set of indices.
  # NOTE: Have helper function that finds valid extensions

  return False

if __name__ == "__main__":
  matrix = [
    ['A', 'B', 'E', 'C'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
  ]
  print(wordSearch(matrix, "ABCCED"))   # True
  print(wordSearch(matrix, "SEE"))   # True
  print(wordSearch(matrix, "ABCB"))   # False