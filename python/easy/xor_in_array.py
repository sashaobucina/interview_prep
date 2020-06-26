def xor(n: int, start: int) -> int:
    """
    # 1486: Given an integer n and an integer start.

    Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

    Return the bitwise XOR of all elements of nums.
    """
    res = start
    for i in range(1, n):
        res ^= (start + (2 * i))

    return res


if __name__ == "__main__":
    assert xor(5, 0) == 8
    assert xor(4, 3) == 8

    print("Passed all tests!")