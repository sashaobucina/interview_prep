from typing import List


def find_min(nums: List[int]) -> int:
    """
    # 154: Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

    Find the minimum element.

    The array may contain duplicates.

    Time complexity: O(logn) -> usually, O(n) in worst case w/ all same elements
    """
    ans = nums[0]
    l, r = 0, len(nums) - 1

    while r > 0 and nums[r] == nums[r - 1]:
        r -= 1

    while l <= r:
        m = l + (r - l) // 2

        if nums[m] < nums[0]:
            ans = nums[m]
            r = m - 1
        else:
            l = m  + 1

    return ans


if __name__ == "__main__":
    nums = [1, 3, 5]
    assert find_min(nums) == 1

    nums = [2, 2, 2, 0, 1]
    assert find_min(nums) == 0

    print("Passed all tests!")
