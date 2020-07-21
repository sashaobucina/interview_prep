from typing import List
from sys import maxsize


def min_subarray_len(s: int, nums: List[int]) -> int:
    """
    # 209: Given an array of n positive integers and a positive integer s, find the minimal length of 
    a contiguous subarray of which the sum ≥ s.

    If there isn't one, return 0 instead.
    """
    res = maxsize

    left, running_sum = 0, 0
    for i in range(len(nums)):
        running_sum += nums[i]

        while running_sum >= s:
            res = min(res, i + 1 - left)

            running_sum -= nums[left]
            left += 1

    return res if res != maxsize else 0


if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    assert min_subarray_len(7, nums) == 2

    print("Passed all tests!")
