import sys
from typing import List


def max_profit(prices: List[int]) -> int:
    """
    # 121: Say you have an array for which the ith element is the price of a given stock on day i.
    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
    design an algorithm to find the maximum profit.

    NOTE: You cannot sell a stock before you buy one.
    """
    minPrice = sys.maxsize
    maxProfit = 0

    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] - minPrice > maxProfit:
            maxProfit = prices[i] - minPrice
    return maxProfit


def max_profit2(prices: List[int]) -> int:
    """
    # 122: Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many transactions as you like
    (i.e., buy one and sell one share of the stock multiple times).

    NOTE: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
    """
    maxProfit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            maxProfit += prices[i] - prices[i-1]

    return maxProfit


def max_profit_w_cooldown(prices: List[int]) -> int:
    """
    # 309: Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
    (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
        - You may not engage in multiple transactions at the same time (ie, you must sell 
        the stock before you buy again).
        - After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

    Time complexity: O(n)
    Space complexity: O(n)
    """
    if not prices:
        return 0

    N = len(prices)

    buy = [0] * (N + 1)
    sell = [0] * (N + 1)
    buy[1] = -prices[0]

    for i in range(1, N):
        buy[i + 1] = max(buy[i], sell[i - 1] - prices[i])
        sell[i + 1] = max(sell[i], buy[i] + prices[i])

    return sell[N]


def max_profit_w_cooldown_best(prices: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if not prices:
        return 0

    buy0 = buy1 = -prices[0]
    sell0 = sell1 = sell2 = 0
    for i in range(1, len(prices)):
        buy0 = max(buy1, sell2 - prices[i])
        sell0 = max(sell1, buy1 + prices[i])

        buy1 = buy0
        sell2 = sell1
        sell1 = sell0

    return sell0


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    assert max_profit(prices) == 5

    prices = [7, 1, 5, 3, 6, 4]
    assert max_profit2(prices) == 7

    prices = [1, 2, 3, 0, 2]
    assert max_profit_w_cooldown(prices) == 3
    assert max_profit_w_cooldown_best(prices) == 3

    print("Passed all tests!")
