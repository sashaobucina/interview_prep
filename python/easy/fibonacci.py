def fib(N: int):
    """
    # 509; Fibonacci numbers are defined as follows:
        F(0) = 0,
        F(1) = 1,
        F(N) = F(N - 1) + F(N - 2), for N > 1.

    Given N, calculate F(N).

    Time complexity: O(n)
    Space complexity: O(n)
    """
    if N == 0:
        return 0
    if N == 1:
        return 1

    memo = [None] * N
    memo[0] = 1
    memo[1] = 1
    for i in range(2, N):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[N-1]


def fib_best(N: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if N == 0:
        return 0

    last_two = [0, 1]
    for i in range(2, N + 1):
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib

    return last_two[1]


if __name__ == "__main__":
    assert fib(0) == fib_best(0) == 0
    assert fib(1) == fib_best(1) == 1
    assert fib(2) == fib_best(2) == 1
    assert fib(5) == fib_best(5) == 5
    assert fib(100) == fib_best(100) == 354224848179261915075

    print("Passed all tests!")
