"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
"""
def convertToTitle(n: int) -> str:
  res = ''
  while n > 0:
    rem = n % 26
    if rem == 0:
      res = 'Z' + res
      n = n // 26 - 1
    else:
      res = chr((rem - 1) + ord('A')) + res
      n = n // 26
  return res

if __name__ == "__main__":
  print(convertToTitle(701))