def sumOfSquares(n: int) -> int:
  squareSum = 0
  while n:
    squareSum += (n % 10) * (n % 10)
    n = n // 10
  return squareSum

def happyNumber(n: int) -> bool:
  slow, fast = n, n
  while True:
    slow = sumOfSquares(slow)
    fast = sumOfSquares(sumOfSquares(fast))
    if fast == slow:
      break
  return slow == 1


if __name__ == "__main__":
  print(happyNumber(21))