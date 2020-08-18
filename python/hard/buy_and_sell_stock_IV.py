from typing import List


def max_profit(k: int, prices: List[int]) -> int:
    """
    # 188: Say you have an array for which the i-th element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete at most k transactions.

    NOTE:
        You may not engage in multiple transactions at the same time (ie, you must sell the stock before 
            you buy again).

    Time complexity: O(N * min(N, 2 * k))
    Space complexity: O(N * min(N, 2 * k))
    """
    if not prices or not k:
        return 0

    N = len(prices)
    if (k * 2) > N:
        res = 0
        for i, j in zip(prices[1:], prices[:-1]):
            res += max(0, i - j)
        return res

    T = k * 2
    memo = [[0 for _ in range(N + 1)] for _ in range(T)]

    for i in range(T):
        memo[i][0] = -float("inf")

    for i in range(N):
        memo[0][i + 1] = max(memo[0][i], -prices[i])
        for j in range(1, T, 2):
            memo[j][i + 1] = max(memo[j][i], memo[j - 1][i] + prices[i])
        for j in range(2, T, 2):
            memo[j][i + 1] = max(memo[j][i], memo[j - 1][i] - prices[i])

    _max = 0
    for i in range(1, T, 2):
        _max = max(_max, memo[i][N])
    return _max


if __name__ == "__main__":
    k = 2
    prices = [2, 4, 1]
    assert max_profit(k, prices) == 2

    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    assert max_profit(k, prices) == 7

    print("Passed all tests!")
