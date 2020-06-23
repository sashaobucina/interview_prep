from typing import List


def array_pair_sum(nums: List[int]) -> int:
    """
    # 561: Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
    say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as 
    large as possible.
    """
    nums.sort()

    total = 0
    for i in range(0, len(nums), 2):
        total += nums[i]

    return total


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    assert array_pair_sum(nums) == 4

    print("Passed all tests!")
