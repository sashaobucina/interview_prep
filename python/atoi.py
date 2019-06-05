"""
We only need to handle four cases:
  - Discards all leading whitespaces
  - Sign of the number
  - Invalid input
  - Overflow
"""
def atoi(s: str) -> int:
  # Strip leading whitespace (1)
  s = s.lstrip(' ')

  if len(s) == 0:
    return 0

  i = base = 0
  sign = 1
  intMax, intMin = 2**31 - 1, -2**31

  # Handle negative numbers (2)
  if s[i] == '-':
    sign = -1
    i += 1
  elif s[i] == '+':
    i += 1

  # Invalid input (3)
  while i < len(s) and s[i] >= '0' and s[i] <= '9':
    base = base * 10 + ord(s[i]) - ord('0')

    # Integer Overflow (4) -- in 32 bit computer
    if base >= intMax and sign == 1:
      return intMax
    if sign == -1 and -base <= intMin:
      return intMin
    i += 1
  return base * sign


if __name__ == "__main__":
  print(atoi("+2147483649"))