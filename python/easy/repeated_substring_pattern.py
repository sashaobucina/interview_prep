def repeated_substring_pattern(s: str) -> bool:
    """
    # 459: Given a non-empty string check if it can be constructed by taking a substring of it and 
    appending multiple copies of the substring together. You may assume the given string consists of 
    lowercase English letters only and its length will not exceed 10000.
    """
    N = len(s)

    for i in range(N // 2):
        substr = s[:i+1]
        div, mod = divmod(N, i+1)

        if (mod == 0) and (substr * div == s):
            return True

    return False


if __name__ == "__main__":
    assert repeated_substring_pattern("abab")
    assert not repeated_substring_pattern("aba")
    assert repeated_substring_pattern("abcabcabcabc")

    print("Passed all tests!")
