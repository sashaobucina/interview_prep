def range_bitwise_and(m: int, n: int) -> int:
    """
    # 201: Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of 
    all numbers in this range, inclusive.
    """
    i = 0
    while m != n:
        m, n, i = m >> 1, n >> 1, i + 1
    print(m, i)
    return m << i


if __name__ == "__main__":
    assert range_bitwise_and(5, 7) == 4

    assert range_bitwise_and(5, 9) == 0

    print("Passed all tests!")