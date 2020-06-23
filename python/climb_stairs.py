def climb_stairs(n: int) -> int:
    """
    # 70: You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    NOTE: Input must be positive.
    """
    if n == 1:
        return 1

    memo = [0] * n

    # handle base cases
    memo[0] = 1
    memo[1] = 2

    # start handling memoized DP cases
    for i in range(2, n):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n - 1]


if __name__ == "__main__":
    assert climb_stairs(2) == 2

    assert climb_stairs(3) == 3

    print("Passed all tests!")
