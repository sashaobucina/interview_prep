from typing import List


def max_profit(prices: List[int], fee: int) -> int:
    """
    # 714: Your are given an array of integers prices, for which the i-th element is the price of a 
    given stock on day i; and a non-negative integer fee representing a transaction fee.

    You may complete as many transactions as you like, but you need to pay the transaction fee for 
    each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the 
    stock share before you buy again.)

    Return the maximum profit you can make.

    Time complexity: O(n)
    Space complexity: O(n) -> can make O(1) w/ auxiliary variables
    """
    if not prices:
        return 0

    N = len(prices)

    held = [-float("inf")] * (N + 1)
    sold = [-float("inf")] * (N + 1)

    sold[0] = 0

    for i in range(N):
        sold[i + 1] = max(sold[i], held[i] + prices[i] - fee)
        held[i + 1] = max(held[i], sold[i] - prices[i])

    return sold[N]


if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    assert max_profit(prices, fee=2) == 8

    print("Passed all tests!")
