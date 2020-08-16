from typing import List


def max_profit_naive(prices: List[int]) -> int:
    """
    # 123: Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete at most two transactions.

    NOTE: You may not engage in multiple transactions at the same time (i.e., you must sell the stock 
    before you buy again).

    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    if not prices:
        return 0

    N = len(prices)
    max_profit = [0] * N

    max_so_far = 0
    min_price = float("inf")
    for i in range(N):
        if prices[i] < min_price:
            min_price = prices[i]
            max_profit[i] = max_so_far
        elif prices[i] - min_price > max_so_far:
            max_so_far = prices[i] - min_price
            max_profit[i] = max_so_far
        else:
            max_profit[i] = max_so_far

    ans = max_profit[0]
    for i in range(N):
        profit = max_profit[i]
        for j in range(i + 1, N):
            ans = max(ans, profit + _find_best(prices[i + 1:]))

    return max(ans, profit)


def _find_best(prices: List[int]) -> int:
    min_price = float("inf")
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit


def max_profit(prices: List[int]) -> int:
    """
    State machine implementation.

    The states are as follows:
        - buy 1st time
        - sell 1st time
        - buy 2nd time
        - sell 2nd time
        - done; completed two transactions

    Time complexity: O(n)
    Space complexity O(n)
    """
    if not prices:
        return 0

    # initialize states
    N = len(prices)
    held1 = [0] * (N + 1)
    sold1 = [0] * (N + 1)
    held2 = [0] * (N + 1)
    sold2 = [0] * (N + 1)
    end = [0] * (N + 1)

    # base cases
    sold1[0] = -float("inf")
    held1[0] = -float("inf")
    sold2[0] = -float("inf")
    held2[0] = -float("inf")
    end[0] = -float("inf")

    # recursive case
    for i in range(N):
        held1[i + 1] = max(held1[i], -prices[i])
        sold1[i + 1] = max(sold1[i], held1[i] + prices[i])
        held2[i + 1] = max(held2[i], sold1[i] - prices[i])
        sold2[i + 1] = held2[i] + prices[i]
        end[i + 1] = max(end[i], sold2[i])

    # max comes from sold1, sold2, or done state
    return max(0, sold1[N], sold2[N], end[N])


if __name__ == "__main__":
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    assert max_profit_naive(prices) == 6
    assert max_profit(prices) == 6

    print("Passed all tests!")
