
from typing import List


def get_row(row_index: int) -> List[int]:
    """
    # 119: Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

    NOTE: The row index starts from 0.

    Space complexity: O(k), as desired
    """
    prev_level = [1]

    curr_len = 2
    for i in range(1, row_index + 1):
        curr_level = [1]
        for j in range(1, curr_len - 1):
            curr_level.append(prev_level[j - 1] + prev_level[j])
        curr_level.append(1)

        prev_level, curr_level = curr_level, []
        curr_len += 1

    return prev_level


if __name__ == "__main__":
    assert get_row(0) == [1]
    assert get_row(1) == [1, 1]
    assert get_row(2) == [1, 2, 1]
    assert get_row(3) == [1, 3, 3, 1]
    assert get_row(4) == [1, 4, 6, 4, 1]

    print("Passed all tests!")
