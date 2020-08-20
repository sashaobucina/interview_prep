def num_decodings(s: str) -> int:
    """
    # 91: A message containing letters from A-Z is being encoded to numbers using the following mapping:

        'A' -> 1
        'B' -> 2
        ...
        'Z' -> 26

    Given a non-empty string containing only digits, determine the total number of ways to decode it.
    """
    def _valid(s: str):
        if "0" in s and s[-1] != "0":
            return False
        return 0 < int(s) < 27

    n = len(s)
    if n == 1:
        return int(_valid(s[0]))

    dp = [0] * n

    # Base case
    dp[0] = int(_valid(s[0]))
    dp[1] = int(_valid(s[:2])) + (dp[0] if int(_valid(s[1])) else 0)

    # Recurrence relation: dp[i] = dp[i - 1] (if s[i] valid else 0) + dp[i - 2] (if s[i-1:i+1] valid else 0),
    for i in range(2, n):
        one_step = dp[i - 1] if _valid(s[i]) else 0
        two_step = dp[i - 2] if _valid(s[i-1:i+1]) else 0

        dp[i] = one_step + two_step

    return dp[n - 1]


if __name__ == "__main__":
    s = "22"
    assert num_decodings(s) == 2

    s = "10"
    assert num_decodings(s) == 1

    s = "1010"
    assert num_decodings(s) == 1

    s = "100000"
    assert num_decodings(s) == 0

    s = "226"
    assert num_decodings(s) == 3

    s = "123452120"
    assert num_decodings(s) == 6

    print("Passed all tests!")
