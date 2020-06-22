from typing import List


def single_number_II(nums: List[int]) -> int:
    """
    # 137: Given a non-empty array of integers, every element appears three times except for one, 
    which appears exactly once. Find that single one.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    return (3 * sum(set(nums)) - sum(nums)) // 2


if __name__ == "__main__":
    nums = [2, 2, 3, 2]
    assert single_number_II(nums) == 3

    nums = [0, 1, 0, 1, 0, 1, 99]
    assert single_number_II(nums) == 99

    print("Passed all tests!")
