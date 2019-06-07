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

if __name__ == "__main__":
  print(pascalsTriangle(6))