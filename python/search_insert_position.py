from typing import List


def search_insert_position(nums: List[int], target: int) -> int:
    """
    # 35: Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.
    """
    for index, num in enumerate(nums):
        if (target <= num):
            return index
    return len(nums)


def search_insert_position_alt(nums: List[int], target: int) -> int:
    """ Algorithm using binary search. """
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo


if __name__ == "__main__":
    nums = [1, 3, 5, 7]
    assert search_insert_position(
        nums, 0) == search_insert_position_alt(nums, 0) == 0
    assert search_insert_position(
        nums, 2) == search_insert_position_alt(nums, 2) == 1
    assert search_insert_position(
        nums, 4) == search_insert_position_alt(nums, 4) == 2
    assert search_insert_position(
        nums, 6) == search_insert_position_alt(nums, 6) == 3
    assert search_insert_position(
        nums, 7) == search_insert_position_alt(nums, 7) == 3
    assert search_insert_position(
        nums, 8) == search_insert_position_alt(nums, 8) == 4

    print("Passed all tests!")
