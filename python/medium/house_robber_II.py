from typing import List


def rob(nums: List[int]) -> int:
    """
    # 213: You are a professional robber planning to rob houses along a street. Each house has a certain 
    amount of money stashed. All houses at this place are arranged in a circle. That means the first house 
    is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will 
    automatically contact the police if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, determine the 
    maximum amount of money you can rob tonight without alerting the police.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    def _rob(nums):
        t1 = 0
        t2 = 0
        for num in nums:
            tmp = t1
            t1 = max(num + t2, t1)
            t2 = tmp

        return t1

    N = len(nums)
    memo = [0 for _ in range(N)]

    return max(_rob(nums[1:]), _rob(nums[:-1]))


if __name__ == "__main__":
    nums = [2, 3, 2]
    assert rob(nums) == 3

    nums = [1, 2, 3, 1]
    assert rob(nums) == 4

    print("Passed all tests!")
