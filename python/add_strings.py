"""
Given two non-negative integers num1 and num2 represented as string, return the sum of 
num1 and num2.

NOTE: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
def add_strings(num1: str, num2: str) -> str:
  i, j = len(num1) - 1, len(num2) - 1
  carry = 0
  sum = ""

  while i >= 0 or j >= 0:
    a = ord(num1[i]) - ord('0') if i >= 0 else 0
    b = ord(num2[j]) - ord('0') if j >= 0 else 0

    sum += str((a + b + carry) % 10)
    carry = (a + b + carry) // 10

    i -= 1
    j -= 1

  if carry:
    sum += '1'

  return sum[::-1]

if __name__ == "__main__":
  sol = add_strings("98", "9")
  print(sol)   # expected: 107
  print(type(sol) is str)    # expected: True