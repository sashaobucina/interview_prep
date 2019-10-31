"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such 
that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).
"""
def numMagicSquaresInside(grid: list) -> int:
  count = 0
  n, m = len(grid), len(grid[0])

  for row in range(n - 2):
    for col in range(m - 2):
      count += 1 if isMagicSquare(grid, row, col) else 0

  return count

def isMagicSquare(grid: list, row: int, col: int) -> bool:
  seen = set()
  gridValues = [grid[row][i] for i in range(col, col + 3)] + \
                [grid[row + 1][i] for i in range(col, col + 3)] + \
                [grid[row + 2][i] for i in range(col, col + 3)]

  if any(value > 9 or value < 1 or value in seen or seen.add(value) for value in gridValues):
    return False

  # get row sums
  rowSum = 0
  for i in range(row, row + 3):
    newSum = sum([grid[i][col], grid[i][col + 1], grid[i][col + 2]])
    if rowSum > 0 and newSum != rowSum:
      return False
    rowSum = newSum

  # get col sums
  colSum = 0
  for i in range(col, col + 3):
    newSum = sum([grid[row][i], grid[row + 1][i], grid[row + 2][i]])
    if colSum > 0 and newSum != colSum:
      return False
    colSum = newSum

  # get diagonal sums
  diagonal = sum([grid[row][col], grid[row+1][col+1], grid[row+2][col+2]])
  diagonalInverse = sum([grid[row][col+2], grid[row+1][col+1], grid[row+2][col]])
  if diagonal != diagonalInverse:
    return False
  diagonalSum = diagonal

  return rowSum == colSum == diagonalSum

if __name__ == "__main__":
  grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
  print(numMagicSquaresInside(grid))  # expected: 1