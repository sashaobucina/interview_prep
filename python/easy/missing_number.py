from typing import List


def missing_number(nums: List[int]) -> int:
    """
    # 268: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

    NOTE: This is my original solution.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    N = len(nums)
    for i in range(N):
        while nums[i] != i and nums[i] != N:
            num = nums[i]
            nums[i], nums[num] = nums[num], nums[i]

    for i in range(N):
        if nums[i] == N:
            return i
    return N


def missing_number_XOR(nums: List[int]) -> int:
    """
    We can harness the fact that XOR is its own inverse to find the missing element in linear time.

    missing = 4 ∧ (0∧0) ∧ (1∧1) ∧ (2∧3) ∧ (3∧4)
            = (4∧4) ∧ (0∧0) ∧ (1∧1) ∧ (3∧3) ∧ 2
            = 0 ∧ 0 ∧ 0 ∧ 0 ∧ 2
            = 2

    Time complexity: O(n)
    Space complexity: O(1)
    """
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num

    return missing


def missing_number_gauss(nums: List[int]) -> int:
    """
    Gauss' formula

    Time complexity: O(n)
    Space complexity: O(1)
    """
    expected_sum = (len(nums) * (len(nums) + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


if __name__ == "__main__":
    nums = [3, 0, 1]
    assert missing_number(nums) == missing_number_XOR(
        nums) == missing_number_gauss(nums) == 2

    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    assert missing_number(nums) == missing_number_XOR(
        nums) == missing_number_gauss(nums) == 8

    print("Passed all tests!")
