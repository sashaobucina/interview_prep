def hamming_distance(x: int, y: int) -> int:
    """
    # 461: The Hamming distance between two integers is the number of positions at which 
    the corresponding bits are different.

    Given two integers x and y, calculate the Hamming distance.
    """
    return bin(x ^ y).count("1")


if __name__ == "__main__":
    assert hamming_distance(1, 4) == 2

    print("Passed all tests!")