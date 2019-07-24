"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
"""
def isUglyNumber(num: int) -> bool:
  if num <= 0:
    return False
  
  while num % 2 == 0:
    num //= 2
  while num % 3 == 0:
    num //= 3
  while num % 5 == 0:
    num //= 5

  return num == 1


if __name__ == "__main__":
  print(isUglyNumber(6))