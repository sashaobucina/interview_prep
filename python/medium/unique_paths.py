"""
Imagine a robot sitting in the top right corner if an NxN grid. The robot can only move right and down. 
How many possible paths can the robot take.
"""
def uniquePath(m: int, n: int) -> int:
  def helper(x: int, y: int) -> int:
    if x == m - 1 and y == n - 1:
      return 1

    rightPath = helper(x + 1, y) if x + 1 < m else 0
    downPath = helper(x, y + 1) if y + 1 < n else 0
    return rightPath + downPath

  if m >= 0 and n >= 0:
    return helper(0, 0)
  return 0

"""
Sub-condition: Imagine certain squares are off limits; such that the robot cant step on them. Design an 
algorithm again to count the number of possible paths.
"""
def uniquePathDP(m: int, n: int) -> int:
  table = [[0 for y in range(n)] for x in range(m)]

  for i in range(m):
    table[i][0] = 1

  for j in range(n):
    table[0][j] = 1

  for i in range(1, m):
    for j in range(1, n):
      table[i][j] = table[i - 1][j] + table[i][j - 1]
  return table[m - 1][n - 1]

if __name__ == "__main__":
  print(uniquePathDP(23, 12))   # Expected solution: 193536720
  # print(uniquePath(23, 12))   # TimeoutError