from collections import deque
from typing import List


def plus_one_hack(digits: List[int]) -> List[int]:
    num = int("".join(map(str, digits))) + 1
    return [int(digit) for digit in str(num)]


def plus_one(digits: List[int]) -> List[int]:
    """
    # 66: Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

    The digits are stored such that the most significant digit is at the head of the list, and each 
    element in the array contain a single digit.

    You may assume the integer does not contain any leading zero, except the number 0 itself.
    """
    q = deque(digits)
    for i in range(len(q) - 1, -1, -1):
        if q[i] < 9:
            q[i] += 1
            return list(q)
        else:
            q[i] = 0

    q.appendleft(1)
    return list(q)


if __name__ == "__main__":
    digits = [3, 9, 9]
    assert plus_one(digits) == [4, 0, 0]

    digits = [2, 1, 9]
    assert plus_one(digits) == [2, 2, 0]

    assert plus_one([9]) == [1, 0]

    print("Passed all tests!")
