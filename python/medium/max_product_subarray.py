from typing import List


def max_product(nums: List[int]) -> int:
    """
    # 152: Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
    which has the largest product.
    """
    if not nums:
        return 0

    global_max = local_min = local_max = nums[0]
    for num in nums[1:]:
        tmp = local_max
        local_max = max(num, local_max * num, local_min * num)
        local_min = min(num, local_min * num, tmp * num)

        global_max = max(global_max, local_max)

    return global_max


if __name__ == "__main__":
    nums = [2,3,-2,4]
    assert max_product(nums) == 6

    nums = [-2, 0, -1]
    assert max_product(nums) == 0

    print("Passed all tests!")