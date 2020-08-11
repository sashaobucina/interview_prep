from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    """
    # 746: On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

    Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach 
    the top of the floor, and you can either start from the step with index 0, or the step with index 1.
    """
    N = len(cost)
    dp = [0 for _ in range(N + 1)]

    # Base cases
    dp[0] = cost[0]
    dp[1] = cost[1]

    # Recurrence relation: dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    for i in range(1, N + 1):
        curr_cost = cost[i] if i < N else 0
        dp[i] = min(dp[i - 1], dp[i - 2]) + curr_cost

    return dp[N]


if __name__ == "__main__":
    cost = [0, 0, 0, 0]
    assert min_cost_climbing_stairs(cost) == 0

    cost = [10, 15, 20]
    assert min_cost_climbing_stairs(cost) == 15

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    assert min_cost_climbing_stairs(cost) == 6

    print("Passed all tests!")
