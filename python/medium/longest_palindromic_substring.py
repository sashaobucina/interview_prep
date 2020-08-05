def longest_palindrome(s: str) -> str:
    """
    # 5: Given a string s, find the longest palindromic substring in s.

    You may assume that the maximum length of s is 1000.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    if not s:
        return ""

    N = len(s)
    start, end = 0, 0
    for i in range(N):
        l1 = _expand_from_center(s, i, i)
        l2 = _expand_from_center(s, i, i + 1)
        max_len = max(l1, l2)
        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start: end + 1]


def _expand_from_center(s: str, left: int, right: int) -> int:
    L, R = left, right
    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1
    return R - L - 1


def longest_palindrome_dp(s: str) -> str:
    """
    This solution uses a DP approach.

    Recurrence relation:
        - T[L][R] = T[L + 1][R - 1] && s[L] == s[R]

    The row indices of the DP table signify the left pointer (L) of the string, and the column indices 
    of the DP table signify the right pointer (R).

    Traverse L (rows) in reverse order, and R (columns) in regular order starting 2 spots from L.

        eg "d  a  b  b  a  d"      -> perform check of T[L][R] == T[L + 1][R - 1] && s[L] && s[R]
            | |_________|  |
            |   L+1, R-1   |
            |              |
            L              R

    Time complexity: O(n^2)
    Space complexity: O(n^2)
    """
    if not s:
        return ""

    N = len(s)
    max_len = 1
    start, end = 0, 0

    # initalize memo table to store overlapping subproblems
    dp = [[0 for _ in range(N)] for _ in range(N)]

    # Base cases: T[L][L] = 1 and T[L][L + 1] = int(s[L] == s[L + 1])
    for L in range(N):
        dp[L][L] = 1
    for L in range(N - 1):
        if s[L] == s[L + 1]:
            dp[L][L + 1] = 1
            max_len, start, end = 2, L, L + 1

    # Recurrence relation: T[L][R] = T[L+1][R-1] && s[L] == s[R]
    for L in range(N - 1, -1, -1):
        for R in range(L + 2, N):
            if dp[L + 1][R - 1] and s[L] == s[R]:
                dp[L][R] = 1

                if (R - L + 1) > max_len:
                    max_len = (R - L + 1)
                    start, end = L, R

    return s[start: end + 1]


if __name__ == "__main__":
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome_dp("cbbd") == "bb"

    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome_dp("babad") in ["bab", "aba"]

    assert longest_palindrome("heracecarls") == "racecar"
    assert longest_palindrome_dp("heracecarls") == "racecar"

    print("Passed all tests!")
