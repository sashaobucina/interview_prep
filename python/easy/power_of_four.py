from math import log2


def is_power_of_four(num: int) -> bool:
    """
    # 342: Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
    """
    curr = 1
    while curr < num:
        curr *= 4

    return curr == num


def is_power_of_four_math(num: int) -> bool:
    """

    """
    return num > 0 and log2(num) % 2 == 0


if __name__ == "__main__":
    assert is_power_of_four(1)
    assert is_power_of_four_math(1)

    assert is_power_of_four(16)
    assert is_power_of_four_math(16)

    assert not is_power_of_four(5)
    assert not is_power_of_four_math(5)

    print("Passed all tests!")