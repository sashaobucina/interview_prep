def find_complement(num: int) -> int:
    """
    # 476: Given a positive integer num, output its complement number. 
    The complement strategy is to flip the bits of its binary representation.
    """
    res = []
    for bit in format(num, "b"):
        res.append(str(int(bit) ^ 1))

    return int("".join(res), 2)


if __name__ == "__main__":
    assert find_complement(5) == 2

    print("Passed all tests!")
