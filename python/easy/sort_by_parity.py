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


def sort_by_parity_II(A: List[int]) -> List[int]:
    """
    # 922: Given an array A of non-negative integers, half of the integers in A are odd, and half of 
    the integers are even.

    Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

    You may return any answer array that satisfies this condition.
    """
    j = 1
    for i in range(0, len(A), 2):
        if A[i] % 2 == 0:
            continue

        while A[j] % 2 == 1:
            j += 2

        A[i], A[j] = A[j], A[i]

    return A


if __name__ == "__main__":
    A = [3, 1, 2, 4]
    assert sort_by_parity(A) == [2, 4, 3, 1]

    A = [4, 2, 5, 7]
    assert sort_by_parity_II(A) == [4, 5, 2, 7]

    print("Passed all tests!")
