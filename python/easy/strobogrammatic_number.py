def is_strobogrammatic(num: str) -> bool:
    """
    # 246: A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

    Write a function to determine if a number is strobogrammatic. The number is represented as a string.
    """
    non_strobogrammatic = {"2", "3", "4", "5", "7"}

    reverse_num = []
    for digit in num:
        if digit in non_strobogrammatic:
            return False

        if digit in {"0", "1", "8"}:
            reverse_num.append(digit)
        elif digit == "6":
            reverse_num.append("9")
        else:
            reverse_num.append("6")

    return "".join(reverse_num[::-1]) == num


if __name__ == "__main__":
    num = "101"
    assert is_strobogrammatic(num)

    num = "69"
    assert is_strobogrammatic(num)

    num = "88"
    assert is_strobogrammatic(num)

    num = "962"
    assert not is_strobogrammatic(num)

    num = "1"
    assert is_strobogrammatic(num)

    print("Passed all tests!")
