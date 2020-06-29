def integer_break(n: int) -> int:
    """
    # 343: Given a positive integer n, break it into the sum of at least two positive integers and 
    maximize the product of those integers. Return the maximum product you can get.
    """
    memo = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(1, i):
            memo[i] = max((i - j) * j, max(memo[i], memo[i - j] * j))

    return memo[n]


if __name__ == "__main__":
    assert integer_break(2) == 1
    assert integer_break(10) == 36

    print("Passed all tests!")
