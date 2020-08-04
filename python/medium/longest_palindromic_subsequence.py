def longest_palindromic_subsequence(s: str) -> int:
    """
    # 516: Given a string s, find the longest palindromic subsequence's length in s.\

    You may assume that the maximum length of s is 1000.
    """
    N = len(s)
    if N <= 1:
        return N

    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = 1

    for i in range(N - 1, -1, -1):
        for j in range(i + 1, N):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][N - 1]


if __name__ == "__main__":
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2

    print("Passed all tests!")
