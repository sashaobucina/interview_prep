"""
Rewrite the given string in a zigzag pattern with the given number or rows.

Draw out string in zigzag format if not sure how the pattern goes.
"""
def zigzagConversion(s: str, numRows: int) -> str:
  if numRows == 1:
    return s

  rows = []
  for i in range(min(numRows, len(s))):
    rows.append([])

  currRow, goingDown = 0, False
  for char in s:
    rows[currRow].append(char)
    if currRow == 0 or currRow == numRows - 1:
      goingDown = not goingDown
    currRow += 1 if goingDown else -1

  # Build final string
  return "".join(["".join([char for char in row]) for row in rows])


if __name__ == "__main__":
  print(zigzagConversion("PAYPALISHIRING", 4))