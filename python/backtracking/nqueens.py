"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both 
indicate a queen and an empty space respectively.
"""
def nqueens(n: int):
  configs = []
  board = [["." for i in range(n)] for i in range(n)]

  def backtrack(board, col):
    if col == n:
      configs.append(["".join(board[i]) for i in range(n)])
      return

    for row in range(n):
      if validSpot(board, row, col):
        board[row][col] = "Q"
        backtrack(board, col + 1)
        board[row][col] = "."

  backtrack(board, 0)
  return configs


def validSpot(board, row, col) -> bool:
  n = len(board)

  # horizontal check
  for i in range(col + 1):
    if board[row][col - i] == "Q":
      return False

  # vertical check
  for i in range(row + 1):
    if board[row - i][col] == "Q":
      return False

  # diagonal checks
  i = 1
  while row - i >= 0 and col - i >= 0:
    if board[row - i][col - i] == "Q":
      return False
    i += 1
  i = 1
  while row + i < n and col - i >= 0:
    if board[row + i][col - i] == "Q":
      return False
    i += 1

  return True

if __name__ == "__main__":
  board = [["Q", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."]]
  print(validSpot(board, 1, 2))
  print(nqueens(4))