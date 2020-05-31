def reverse_int(x: int) -> int:
    """
    # 7: Given a 32-bit signed integer, reverse digits of an integer.
    """
    is_negative = False
    if x < 0:
        is_negative = True
        x = -x

    reverse, prev = 0, 0
    while x != 0:
        curr = x % 10
        reverse = (reverse * 10) + curr

        # check for overflow
        if reverse >= 2147483647 or reverse <= -2147483648:
            reverse = 0
        if ((reverse - curr) // 10) != prev:
            print("WARNING: Integer passed in produced overflow!")
            return 0

        prev = reverse
        x //= 10

    return -reverse if is_negative else reverse


if __name__ == "__main__":
    assert reverse_int(321) == 123
    assert reverse_int(-123) == -321
    assert reverse_int(120) == 21
    assert reverse_int(1534236469) == 0

    print("Passed all tests!")
