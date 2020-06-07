from typing import List


def waysToPay(coins: set, n: int, startCoin: int) -> int:
    """
    Find the number of unique ways to pay using an infinite set of given coins.
    """
    if n == 0:
        return 1
    if n < 0:
        return 0

    nCoins = 0
    for coin in range(startCoin, len(coins)):
        nCoins += waysToPay(coins, n - coins[coin], coin)
    return nCoins


def waysToPayDP(coins: set, n: int):
    """
    Dynamic Programming sol'n
    """
    m = len(coins)
    table = [[0 for x in range(m)] for y in range(n + 1)]

    # Populate the state table with base case when n is 0.
    for i in range(m):
        table[0][i] = 1

    for i in range(1, n + 1):
        for j in range(m):
            x = table[i - coins[j]][j] if i - \
                coins[j] >= 0 else 0    # use the current coin
            # go to the next coin in the set
            y = table[i][j - 1] if j >= 1 else 0

            table[i][j] = x + y

    return table[n][m - 1]


def coin_change_II(amount: int, coins: List[int]) -> int:
    """
    # 518: You are given coins of different denominations and a total amount of money. 
    Write a function to compute the number of combinations that make up that amount. 
    You may assume that you have infinite number of each kind of coin.
    """
    memo = [0] * (amount + 1)
    memo[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            memo[i] += memo[i - coin]

    return memo[amount]


if __name__ == "__main__":
    coins = (1, 5, 10, 25)
    assert waysToPayDP(coins, 40) == waysToPay(coins, 40, 0) == 31

    coins = [1, 2, 5]
    assert coin_change_II(5, coins) == 4

    print("Passed all tests!")
