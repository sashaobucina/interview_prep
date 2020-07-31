def title_to_number(s: str) -> int:
    """
    # 171: Given a column title as appear in an Excel sheet, return its corresponding column number.

    For example:
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28 
        ...
    """
    ans = 0
    for i in range(len(s)):
        ans *= 26
        ans += ord(s[i]) - ord('A') + 1

    return ans


if __name__ == "__main__":
    assert title_to_number("A") == 1
    assert title_to_number("AB") == 28
    assert title_to_number("ZY") == 701

    print("Passed all tests!")
