def max_power(s: str) -> int:
    """
    # 1446: Given a string s, the power of the string is the maximum length of a non-empty substring 
    that contains only one unique character.

    Return the power of the string.
    """
    if not s:
        return 0

    power = 1
    curr_power = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            curr_power += 1
        else:
            power = max(power, curr_power)
            curr_power = 1

    return max(power, curr_power)


if __name__ == "__main__":
    assert max_power("") == 0
    assert max_power("a") == 1
    assert max_power("leetcode") == 2
    assert max_power("abbcccddddeeeeedcba") == 5

    print("Passed all tests!")
