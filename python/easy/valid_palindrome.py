def is_palindrome(s: str) -> bool:
    """
    # 125: Given a string, determine if it is a palindrome, considering only alphanumeric characters 
    and ignoring cases.

    NOTE: For the purpose of this problem, we define empty string as valid palindrome.
    """
    s = s.lower()

    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo].isalnum() and s[hi].isalnum():
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
            continue

        if not s[lo].isalnum():
            lo += 1
        if not s[hi].isalnum():
            hi -= 1

    return True


if __name__ == "__main__":
    assert is_palindrome("")
    assert is_palindrome("racecar")
    assert is_palindrome("aba_")

    assert not is_palindrome("0P")
    assert not is_palindrome("hello")
    assert not is_palindrome("5racecare")

    print("Passed all tests!")
