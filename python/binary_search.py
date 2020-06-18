from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """
    # 704: Given a sorted (in ascending order) integer array nums of n elements and a target value, write 
    a function to search target in nums. If target exists, then return its index, otherwise return -1.
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid

        if target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    assert binary_search(nums, target=5) == 4

    nums = [-1, 0, 3, 5, 9, 12]
    assert binary_search(nums, target=2) == -1

    nums = [-1, 0, 3, 5, 9, 12]
    assert binary_search(nums, target=-2) == -1

    nums = [-1, 0, 3, 5, 9, 12]
    assert binary_search(nums, target=13) == -1

    print("Passed all tests!")
