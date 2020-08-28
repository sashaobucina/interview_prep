from typing import List


def sum_of_digits(A: List[int]) -> int:
    """
    # 1085: Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.

    Return 0 if S is odd, otherwise return 1.
    """
    digits = []
    num = min(A)

    while num > 0:
        digits.append(num % 10)
        num //= 10

    return 1 if sum(digits) % 2 == 0 else 0


if __name__ == "__main__":
    A = [34, 23, 1, 24, 75, 33, 54, 8]
    assert not sum_of_digits(A)

    A = [99, 77, 33, 66, 55]
    assert sum_of_digits(A)

    print("Passed all tests!")
