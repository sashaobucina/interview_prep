def is_power_of_three(n: int) -> bool:
    """
    # 326: Given an integer, write a function to determine if it is a power of three.
    """
    if n == 0:
        return False

    curr = n
    while curr % 3 == 0:
        curr //= 3

    return curr == 1


if __name__ == "__main__":
    assert is_power_of_three(1)
    assert is_power_of_three(3)
    assert is_power_of_three(27)
    assert not is_power_of_three(28)
    assert not is_power_of_three(0)
    assert not is_power_of_three(-3)
    assert not is_power_of_three(-28)

    print("Passed all tests!")
