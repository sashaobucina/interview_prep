from typing import List


def max_profit(prices: List[int]) -> int:
    """
    # 122: Say you have an array prices for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
    (i.e., buy one and sell one share of the stock multiple times).

    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
    """
    # peak and valley technique
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    assert max_profit(prices) == 7

    prices = [1, 2, 3, 4, 5]
    assert max_profit(prices) == 4

    prices = [7, 6, 4, 3, 1]
    assert max_profit(prices) == 0

    print("Passed all tests!")
