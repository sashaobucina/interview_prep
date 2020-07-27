from typing import List


def find_peak_element(nums: List[int]) -> int:
    """
    # 162: A peak element is an element that is greater than its neighbors.
    Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

    The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
    You may imagine that nums[-1] = nums[n] = -∞.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    N = len(nums)

    if N == 1 or nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return N - 1

    for i in range(1, N - 1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return i

    return -1


def find_peak_element_follow_up(nums: List[int]) -> int:
    """
    Follow up: Your solution should be in logarithmic complexity

    Time complexity: O(logn)
    Space complexity: O(1)
    """
    ans = -1
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if m == 0 or nums[m] > nums[m - 1]:
            ans = m
            l = m + 1
        else:
            r = m - 1

    return ans


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    assert find_peak_element(nums) == 2
    assert find_peak_element_follow_up(nums) == 2

    nums = [1, 2, 1, 3, 5, 6, 4]
    assert find_peak_element(nums) == 1
    assert find_peak_element_follow_up(nums) == 5

    print("Passed all tests!")
