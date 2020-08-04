def is_valid_palindrome(s: str, k: int) -> bool:
    """
    # 1216: Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

    A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.
    """
    N = len(s)
    if N <= 1:
        return True

    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = 1

    for i in range(N - 1, -1, -1):
        for j in range(i + 1, N):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][N - 1] + k >= N


if __name__ == "__main__":
    assert is_valid_palindrome("abcdeca", 2)
    assert is_valid_palindrome("agbdba", 1)
    assert not is_valid_palindrome("ab", 0)

    print("Passed all tests!")