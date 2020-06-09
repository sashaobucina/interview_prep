def is_subsequence(s: str, t: str) -> bool:
    """
    # 392: Given a string s and a string t, check if s is subsequence of t.

    A subsequence of a string is a new string which is formed from the original string by deleting some 
    (can be none) of the characters without disturbing the relative positions of the remaining characters. 
    (ie, "ace" is a subsequence of "abcde" while "aec" is not).
    """
    i, j = 0, 0
    while i < len(t) and j < len(s):
        if t[i] == s[j]:
            j += 1
        i += 1

    return j == len(s)


if __name__ == "__main__":
    t = "ahbgdc"

    assert is_subsequence("", t)
    assert is_subsequence("abc", t)
    assert not is_subsequence("axc", t)

    print("Passed all tests!")