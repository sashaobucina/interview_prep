from typing import List


def sort_by_parity(A: List[int]) -> List[int]:
    """
    # 905: Given an array A of non-negative integers, return an array consisting of all the even 
    elements of A, followed by all the odd elements of A.

    You may return any answer array that satisfies this condition.
    """
    even, odd = [], []
    for num in A:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even + odd


if __name__ == "__main__":
    A = [3, 1, 2, 4]
    assert sort_by_parity(A) == [2, 4, 3, 1]

    print("Passed all tests!")
