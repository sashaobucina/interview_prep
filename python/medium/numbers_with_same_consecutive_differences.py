from typing import List


def nums_same_consec_diff(N: int, K: int) -> List[int]:
    """
    # 967: Return all non-negative integers of length N such that the absolute difference between every 
    two consecutive digits is K.

    NOTE: Every number in the answer must not have leading zeros except for the number 0 itself. 
    For example, 01 has one leading zero and is invalid, but 0 is valid.

    You may return the answer in any order.
    """
    if not N:
        return []

    res = []

    def _backtrack(num: int, n: int):
        if n == N:
            res.append(num)
            return

        last_digit = num % 10

        if K == 0:
            _backtrack(num * 10 + last_digit, n + 1)
        else:
            if last_digit + K < 10:
                new_num = (num * 10) + (last_digit + K)
                _backtrack(new_num, n + 1)
            if last_digit - K > -1:
                new_num = (num * 10) + (last_digit - K)
                _backtrack(new_num, n + 1)

    start_idx = 1 if N > 1 else 0
    for digit in range(start_idx, 10):
        _backtrack(digit, 1)

    return sorted(res)


if __name__ == "__main__":
    N, K = 3, 7
    assert nums_same_consec_diff(N, K) == [181, 292, 707, 818, 929]

    N, K = 2, 1
    assert nums_same_consec_diff(
        N, K) == [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]

    N, K = 1, 0
    assert nums_same_consec_diff(N, K) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    N, K = 2, 0
    assert nums_same_consec_diff(N, K) == [11, 22, 33, 44, 55, 66, 77, 88, 99]

    print("Passed all tests!")
