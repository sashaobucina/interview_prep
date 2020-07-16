import math


def my_pow(x: float, n: int) -> float:
    """
    # 50: Implement pow(x, n), which calculates x raised to the power n (xn).
    """
    if n == 0:
        return 1

    if n == 1:
        return x

    if n < 0:
        return 1 / my_pow(x, -n)

    tmp = my_pow(x, n // 2)
    if n % 2 == 0:
        return tmp * tmp
    else:
        return x * tmp * tmp


if __name__ == "__main__":
    assert my_pow(2.00000, -2) == 0.25000
    assert my_pow(2.00000, 10) == 1024.0000
    assert math.isclose(my_pow(2.10000, 3), 9.26100)

    print("Passed all tests!")
