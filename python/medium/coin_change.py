"""
Find the number of unique ways to pay using an infinite set of given coins.
"""
def waysToPay(coins: set, n: int, startCoin: int) -> int:
  if n == 0:
    return 1
  if n < 0:
    return 0

  nCoins = 0
  for coin in range(startCoin, len(coins)):
    nCoins += waysToPay(coins, n - coins[coin], coin)
  return nCoins

"""
Dynamic Programming
"""
def waysToPayDP(coins: set, n: int):
  m = len(coins)
  table = [[0 for x in range(m)] for y in range(n + 1)]

  # Populate the state table with base case when n is 0.
  for i in range(m):
    table[0][i] = 1

  for i in range(1, n + 1):
    for j in range(m):
      x = table[i - coins[j]][j] if i - coins[j] >= 0 else 0    # use the current coin
      y = table[i][j - 1] if j >= 1 else 0    # go to the next coin in the set

      table[i][j] = x + y

  return table[n][m - 1]

if __name__ == "__main__":
  coins = (1, 5, 10, 25)
  print(waysToPay(coins, 40, 0))
  print(waysToPayDP(coins, 40))