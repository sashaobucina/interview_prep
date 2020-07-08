from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    # 15: Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

    NOTE: The solution set must not contain duplicate triplets.
    """
    res = []
    nums.sort()

    n = len(nums)
    for i in range(n-2):

        # skip duplicate starting points
        if i > 0 and nums[i-1] == nums[i]:
            continue

        lo, hi = i + 1, n - 1
        while lo < hi:
            summed = nums[i] + nums[lo] + nums[hi]
            
            if summed == 0:
                res.append([nums[i], nums[lo], nums[hi]])
                
                # skip duplicates
                while lo < hi and nums[lo] == nums[lo + 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi - 1]:
                    hi -= 1
                lo += 1
                hi -= 1

            elif summed > 0:
                hi -= 1
            else:
                lo += 1

    return res


def three_sum_smaller(nums: List[int], target: int) -> int:
    """ # 259 """
    counter = 0
    nums.sort()
    for i in range(len(nums) - 1):
        counter += two_sum_smaller(nums, i + 1, target - nums[i])
    return counter


def two_sum_smaller(nums: List[int], startInd: int, target: int) -> int:
    sum = 0
    left, right = startInd, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            sum += right - left
            left += 1
        else:
            right -= 1

    return sum


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    assert threeSum(arr) == [[-1, -1, 2], [-1, 0, 1]]

    arr2 = [-2, -2, 0, 1, 3]
    assert three_sum_smaller(arr2, 2) == 7

    print("Passed all tests!")
