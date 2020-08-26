from typing import List


def single_non_duplicate(nums: List[int]) -> int:
    """
    # 540: You are given a sorted array consisting of only integers where every element appears exactly 
    twice, except for one element which appears exactly once. Find this single element that appears only once.

    Follow up: Your solution should run in O(log n) time and O(1) space.
    """
    N = len(nums)
    lo, hi = 0, N - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        halves_are_even = (hi - mid) % 2 == 0

        if nums[mid + 1] == nums[mid]:
            if halves_are_even:
                lo = mid + 2
            else:
                hi = mid - 1
        elif nums[mid - 1] == nums[mid]:
            if halves_are_even:
                hi = mid - 2
            else:
                lo = mid + 1
        else:
            return nums[mid]

    return nums[lo]


if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    assert single_non_duplicate(nums) == 2

    nums = [3, 3, 7, 7, 10, 11, 11]
    assert single_non_duplicate(nums) == 10

    print("Passed all tests!")
