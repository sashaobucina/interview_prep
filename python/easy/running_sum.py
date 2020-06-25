from typing import List


def running_sum(nums: List[int]) -> List[int]:
    """
    # 1480: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.
    """
    summed = [nums[0]]
    for i in range(1, len(nums)):
        summed.append(nums[i] + summed[i - 1])

    return summed


if __name__ == "__main__":
    nums = [3, 1, 2, 10, 1]
    assert running_sum(nums) == [3, 4, 6, 16, 17]

    print("Passed all tests!")
