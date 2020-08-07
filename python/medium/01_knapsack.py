from typing import List


def knapsack(values: List[int], weights: List[int], capacity: int) -> int:
    """
    Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum 
    total value in the knapsack.

    In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights 
    associated with n items respectively. Also given an integer capacity which represents knapsack capacity, 
    find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to capacity.

    You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
    """
    N = len(values)

    # Base case & initialization
    memo = [[0 for _ in range(capacity + 1)] for _ in range(N + 1)]

    # Recursive case
    for i in range(1, N + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                memo[i][w] = memo[i - 1][w]
            else:
                memo[i][w] = max(memo[i - 1][w], memo[i - 1]
                                [w - weights[i - 1]] + values[i - 1])

    return memo[N][capacity]


if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [1, 2, 3]
    assert knapsack(values, weights, 4) == 180
    assert knapsack(values, weights, 5) == 220

    print("Passed all tests!")
