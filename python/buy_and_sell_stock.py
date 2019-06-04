import sys

"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""
def max_profit(prices: list) -> int:
  minPrice = sys.maxsize
  maxProfit = 0

  for i in range(len(prices)):
    if prices[i] < minPrice:
      minPrice = prices[i]
    elif prices[i] - minPrice > maxProfit:
      maxProfit = prices[i] - minPrice
  return maxProfit

"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
def max_profit2(prices: list) -> int:
  maxProfit = 0
  for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
      maxProfit += prices[i] - prices[i-1]
  return maxProfit

  """ Other way to solve problem - peak and valley solution """
  # if len(prices) <= 1:
  #   return 0

  # maxProfit = 0
  # i = 0
  # valley = prices[0]
  # peak = prices[0]
  # while i < len(prices) - 1:
  #   while i < len(prices) - 1 and prices[i] >= prices[i+1]:
  #     i += 1
  #   valley = prices[i]
  #   while (i < len(prices) - 1 and prices[i] <= prices[i+1]):
  #     i += 1
  #   peak = prices[i]
  #   maxProfit += peak - valley
  # return maxProfit

if __name__ == "__main__":
  arr = [7, 1, 5, 3, 6, 4]
  print(max_profit(arr))

  arr2 = [7, 1, 5, 3, 6, 4]
  print(max_profit2(arr))