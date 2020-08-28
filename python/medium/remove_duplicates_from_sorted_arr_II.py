from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    # 80: Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most 
    twice and return the new length.

    Do not allocate extra space for another array, you must do this by modifying the input array in-place 
    with O(1) extra memory.
    """
    w = r = 2
    while r < len(nums):
        if nums[r] != nums[w - 2]:
            nums[w] = nums[r]
            w += 1
        r += 1

    return w


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    idx = remove_duplicates(nums)
    assert nums[:idx] == [1, 1, 2, 2, 3]

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    idx = remove_duplicates(nums)
    assert nums[:idx] == [0, 0, 1, 1, 2, 3, 3]

    print("Passed all tests!")
