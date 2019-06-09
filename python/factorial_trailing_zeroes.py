"""
Given an integer n, return the number of trailing zeroes in n!.
"""
def trailingZeroes(n: int) -> int:
  count, i = 0, 5
  while n // i >= 1:
    count += n // i
    i *= 5
  return count

if __name__ == "__main__":
  print(trailingZeroes(100))