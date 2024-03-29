from typing import List


def singleNumber(nums: List[int]) -> int:
    """
    # 136: Given a non-empty array of integers, every element appears twice except for one. 
    Find that single one.
    """
    return 2 * sum(set(nums)) - sum(nums)


def singleNumberXOR(nums: List[int]) -> int:
    bitmask = 0
    for num in nums:
        bitmask ^= num

    return bitmask


if __name__ == "__main__":
    nums = [2, 2, 4, 1, 1]
    assert singleNumber(nums) == 4
    assert singleNumberXOR(nums) == 4

    print("Passed all tests!")
