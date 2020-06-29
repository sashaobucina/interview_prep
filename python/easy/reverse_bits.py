def reverse_bits(n: int) -> int:
    """
    # 190: Reverse bits of a given 32 bits unsigned integer.
    """
    ret, power = 0, 31
    while n:
        ret += (n & 1) << power
        n = n >> 1
        power -= 1

    return ret


if __name__ == "__main__":
    assert reverse_bits(43261596) == 964176192

    print("Passed all tests!")
