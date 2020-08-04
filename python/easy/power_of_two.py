def is_power_of_two(num: int) -> bool:
    """
    # 231: Given an integer, write a function to determine if it is a power of two.
    """
    curr = 1
    while curr < num:
        curr *= 2

    return curr == num


def is_power_of_two_math(num: int) -> bool:
    """
    Any power of 2 minus 1 is all ones: (2 N - 1 = 111....b)

    Take 8 for example. 1000 & 0111 = 0000

    So that expression tests if a number is NOT a power of 2.
    """
    return num > 0 and not (num & (num - 1))


if __name__ == "__main__":
    assert is_power_of_two(1)
    assert is_power_of_two_math(1)
    assert is_power_of_two(2)
    assert is_power_of_two_math(2)
    assert is_power_of_two(32)
    assert is_power_of_two_math(32)
    assert is_power_of_two(128)
    assert is_power_of_two_math(128)

    assert not is_power_of_two(0)
    assert not is_power_of_two_math(0)
    assert not is_power_of_two(3)
    assert not is_power_of_two_math(3)
    assert not is_power_of_two(122)
    assert not is_power_of_two_math(122)

    print("Passed all tests!")