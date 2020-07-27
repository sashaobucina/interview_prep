from typing import List


def find_min(nums: List[int]) -> int:
    """
    # 153: Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

    Find the minimum element.

    You may assume no duplicate exists in the array.

    Time complexity: O(logn)
    """
    ans = nums[0]
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] < nums[0]:
            ans = nums[mid]
            hi = mid - 1
        else:
            lo = mid + 1

    return ans


if __name__ == "__main__":
    nums = [7, 1, 2, 3, 4, 5, 6]
    assert find_min(nums) == 1

    print("Passed all tests!")
