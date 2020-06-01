from typing import List


def move_zeros(nums: List[int]) -> None:
    """
    # 283: Given an array nums, write a function to move all 0's to the end of it 
    while maintaining the relative order of the non-zero elements.
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count], nums[i] = nums[i], nums[count]
            count += 1


if __name__ == "__main__":
    nums = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    move_zeros(nums)
    assert nums == [1, 9, 8, 4, 2, 7, 6, 9, 0, 0, 0, 0, 0]

    print("Passed all tests!")
