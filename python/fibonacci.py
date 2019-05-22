"""
Dynamic programming solution to fibonacci sequence - O(n)
"""
def fib(n: int):
  if n == 1 or n == 2:
    return 1
  memo = [None] * n
  memo[0] = 1
  memo[1] = 1
  for i in range(2, n):
    memo[i] = memo[i-1] + memo[i-2]
  return memo[n-1]

if __name__ == "__main__":
  print(fib(1000))