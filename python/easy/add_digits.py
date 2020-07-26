def add_digits(num: int) -> int:
    """
    # 258: Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
    """
    def _add(n: int) -> int:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10

        return sum(digits)


    while num // 10 > 0:
        num = _add(num)

    return num


if __name__ == "__main__":
    assert add_digits(38) == 2
    assert add_digits(152) == 8


    print("Passed all tests!")