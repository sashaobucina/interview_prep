from typing import List


def first_missing_positive(nums: List[int]) -> int:
    """
    # 41: Given an unsorted integer array, find the smallest missing positive integer.

    Follow up: Your algorithm should run in O(n) time and uses constant extra space.
    """
    if not nums:
        return 1

    i = 0
    n = len(nums)
    while i < n:
        while 0 < nums[i] <= n and (nums[i] - 1) != i and nums[nums[i] - 1] != nums[i]:
            num = nums[i]
            nums[i], nums[num - 1] = nums[num - 1], nums[i]

        i += 1

    idx = 1
    for i in range(n):
        if idx != nums[i]:
            return idx

        idx += 1

    return idx


if __name__ == "__main__":
    nums = [0, 1, 2]
    assert first_missing_positive(nums)

    nums = [-1, 4, -1, 1]
    assert first_missing_positive(nums) == 2

    nums = [7, 8, 9, 10, 11]
    assert first_missing_positive(nums) == 1

    nums = [1, 1]
    assert first_missing_positive(nums) == 2

    print("Passed all tests!")
