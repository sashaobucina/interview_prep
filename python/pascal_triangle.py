def pascalsTriangle(numRows: int) -> list:
  res = []
  for line in range(numRows):
    currRow = []
    for i in range(line + 1):
      currRow.append(binomialCoeff(line, i))
    res.append(currRow)
  return res

def binomialCoeff(n: int, k: int) -> int:
  res = 1
  if k > n - k:
    k = n - k
  for i in range(k):
    res = res * (n-i)
    res = res // (i+1)
  return res

"""
Time Complexity: O(numRows^2)
"""
def pascalsTriangleDP(numRows: int) -> list:
  triangle = []
  for rowNum in range(numRows):
    row = [None for _ in range(rowNum+1)]
    row[0], row[-1] = 1, 1
    for j in range(1, len(row) - 1):
      row[j] = triangle[rowNum - 1][j-1] + triangle[rowNum - 1][j]
    triangle.append(row)
  return triangle

if __name__ == "__main__":
  print(pascalsTriangleDP(6))