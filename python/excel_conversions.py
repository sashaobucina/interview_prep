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

def titleToNumber(s: str) -> int:
  res = 0
  for i in range(len(s)):
    res *= 26
    res += ord(s[i]) - ord('A') + 1

  return res

if __name__ == "__main__":
  print(convertToTitle(701))
  print(titleToNumber('WB'))