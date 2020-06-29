from typing import List


def cut_rod(n: int, prices: List[int]) -> int:
    """
    Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. 
    Determine the maximum value obtainable by cutting up the rod and selling the pieces.
    """
    memo = [-float("inf")] * (n + 1)
    memo[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            memo[i] = max(memo[i], prices[j] + memo[i - j - 1])

    return memo[n]


if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert cut_rod(8, prices) == 22

    print("Passed all tests!")
