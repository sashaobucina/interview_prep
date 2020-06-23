from typing import List
from sys import maxsize


def max_subarray(nums: List[int]) -> int:
    """
    # 53: Given an integer array nums, find the contiguous subarray 
    (containing at least one number) which has the largest sum and return its sum.
    """
    max_so_far = -maxsize - 1
    max_ending_here = 0

    for i in range(len(nums)):
        max_ending_here += nums[i]

        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


def max_subarray_dp(nums: List[int]) -> int:
    """
    NOTE: Kadane's algorithm -> T[n] = max(A[n], T[n-1] + A[n])
    """
    max_so_far = nums[0]
    curr_max = nums[0]

    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max + nums[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


if __name__ == "__main__":
    nums = [-13, -3, -15, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    assert max_subarray(nums) == max_subarray_dp(nums) == -3

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray(nums) == max_subarray_dp(nums) == 6

    print("Passed all tests!")
