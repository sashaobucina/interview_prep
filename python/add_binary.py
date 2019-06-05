"""

"""
def addBinary(a: str, b: str) -> str:
  res = ""
  remainder = 0
  max_len = max(len(a), len(b))
  for i in range(max_len):
    idx1 = len(a) - 1 - i
    idx2 = len(b) - 1 - i
    n1 = 1 if idx1 >= 0 and a[idx1] == "1" else 0
    n2 = 1 if idx2 >= 0 and b[idx2] == "1" else 0
    sum = n1 + n2 + remainder

    # Calculate sum and remainder
    if sum == 3:
      sum = 1
      remainder = 1
    elif sum == 2:
      sum = 0
      remainder = 1
    else:
      remainder = 0

    res = str(sum) + res

  if remainder == 1:
    res = str(1) + res
  return res

if __name__ == "__main__":
  print(addBinary("1", "11"))