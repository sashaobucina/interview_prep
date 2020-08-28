from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    # 26: Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    """
    w, r = 1, 1
    while r < len(nums):
        if nums[r] != nums[r - 1]:
            nums[w] = nums[r]
            w += 1
        r += 1

    return w


if __name__ == "__main__":
    nums = [1, 1, 2]
    idx = remove_duplicates(nums)
    assert nums[:idx] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    idx = remove_duplicates(nums)
    assert nums[:idx] == [0, 1, 2, 3, 4]

    print("Passed all tests!")
