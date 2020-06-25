from typing import List


def find_duplicate(nums: List[int]) -> int:
    """
    # 287: Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
    prove that at least one duplicate number must exist.

    Assume that there is only one duplicate number, find the duplicate one

    NOTE:
        - You must not modify the array (assume the array is read only).
        - You must use only constant, O(1) extra space.
        - Your runtime complexity should be less than O(n2).
        - There is only one duplicate number in the array, but it could be repeated more than once.
    """
    # Naive implementation - sort the list and check adjacent entries
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]:
            return nums[i]

    return -1


def find_duplicate(nums: List[int]) -> int:
    """
    NOTE: This solution uses Floyd's cycle detection algorithm.
    """
    hare, tortoise = nums[0], nums[0]

    # phase 1: loop until two pointers meet, guaranteed in cycle
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # phase 2: reset slow pointer, and increment both equally to meet at cycle entrance
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    assert find_duplicate(nums) == 2

    nums = [3, 1, 3, 4, 2]
    assert find_duplicate(nums) == 3

    nums = [2, 2, 2, 2]
    assert find_duplicate(nums) == 2

    print("Passed all tests!")
