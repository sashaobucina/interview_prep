from typing import List


def max_profit(prices: List[int]) -> int:
    """
    # 121: Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
    design an algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.
    """
    if not prices:
        return 0

    min_price = prices[0]
    profit = 0

    for price in prices[1:]:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    assert max_profit(prices) == 5

    prices = [7, 6, 4, 3, 1]
    assert max_profit(prices) == 0

    print("Passed all tests!")
