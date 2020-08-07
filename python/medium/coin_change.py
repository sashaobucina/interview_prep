from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    # 322: You are given coins of different denominations and a total amount of money amount.

    Write a function to compute the fewest number of coins that you need to make up that amount. 
    If that amount of money cannot be made up by any combination of the coins, return -1.
    """
    memo = [float("inf") for _ in range(amount + 1)]
    memo[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            # Recurrence relation: T[amt] = min(T[amt], T[amt - coin] + 1)
            memo[i] = min(memo[i], memo[i - coin] + 1)

    return memo[amount] if memo[amount] != float("inf") else -1


def ways_to_pay(coins: set, n: int, startCoin: int) -> int:
    """
    Find the number of unique ways to pay using an infinite set of given coins.
    """
    if n == 0:
        return 1
    if n < 0:
        return 0

    nCoins = 0
    for coin in range(startCoin, len(coins)):
        nCoins += ways_to_pay(coins, n - coins[coin], coin)
    return nCoins


def ways_to_pay_dp(coins: set, n: int):
    """
    Dynamic Programming sol'n
    """
    m = len(coins)
    memo = [[0 for _ in range(n + 1)] for _ in range(m)]
    for i in range(m):
        memo[i][0] = 1

    for i in range(m):
        for j in range(1, n + 1):
            # number of ways to amount including this coin
            with_coin = memo[i][j - coins[i]] if j - coins[i] >= 0 else 0

            # number of ways to get to amount not including this coin
            prev = memo[i - 1][j] if i - 1 >= 0 else 0

            memo[i][j] = with_coin + prev

    return memo[m - 1][n]


if __name__ == "__main__":
    # Leetcode coin change problem (# 322)
    coins = [1, 2, 5]
    assert coin_change(coins, 11) == 3

    coins = [2]
    assert coin_change(coins, 3) == -1

    # classic coin change problem (GeeksForGeeks DP-7)
    coins = [1, 5, 10, 25]
    assert ways_to_pay_dp(coins, 40) == ways_to_pay(coins, 40, 0) == 31

    print("Passed all tests!")
