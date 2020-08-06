from typing import List


def change(amount: int, coins: List[int]) -> int:
    """
    # 518: You are given coins of different denominations and a total amount of money.

    Write a function to compute the number of combinations that make up that amount. 
    You may assume that you have infinite number of each kind of coin.

    NOTE: Similar to climb stairs problem w/ dynamic set of available steps to take. (DP)
    """
    memo = [0] * (amount + 1)
    memo[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            memo[i] += memo[i - coin]

    return memo[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    assert change(5, coins) == 4

    print("Passed all tests!")