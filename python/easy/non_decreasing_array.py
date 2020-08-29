from typing import List


def check_possibility(nums: List[int]) -> bool:
    """
    # 665: Given an array nums with n integers, your task is to check if it could become non-decreasing 
    by modifying at most 1 element.

    We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
    """
    p = None
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if p is not None:
                return False
            p = i

    return (p is None) or (p == 0) or (p == len(nums) - 2) or (nums[p - 1] <= nums[p + 1]) or (nums[p] <= nums[p + 2])


if __name__ == "__main__":
    # no problem index
    nums = [1, 2, 4]
    assert check_possibility(nums)

    # more than one problem index
    nums = [4, 2, 1]
    assert not check_possibility(nums)

    # single bad problem index
    nums = [3, 4, 2, 3]
    assert not check_possibility(nums)

    # single good problem index
    nums = [8, 1, 3, 4, 6]
    assert check_possibility(nums)

    nums = [2, 4, 4, 5, 6, 2]
    assert check_possibility(nums)

    nums = [1, 2, 4, 0, 5, 6]
    assert check_possibility(nums)

    print("Passed all tests!")
