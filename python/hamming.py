def hamming_distance(x: int, y: int) -> int:
    """
    # 461: The Hamming distance between two integers is the number of positions at which 
    the corresponding bits are different.

    Given two integers x and y, calculate the Hamming distance.
    """
    return bin(x ^ y).count("1")


def hamming_weight(n: int) -> int:
    """
    # 191: Write a function that takes an unsigned integer and return the number of '1' bits it has 
    (also known as the Hamming weight).
    """
    count = 0
    while n != 0:
        n &= n - 1
        count += 1

    return count


if __name__ == "__main__":
    assert hamming_weight(11) == 3
    assert hamming_distance(1, 4) == 2

    print("Passed all tests!")
