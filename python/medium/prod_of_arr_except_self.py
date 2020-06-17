from typing import List


def prod_except_self(nums: List[int]) -> List[int]:
    """
    # 238: Given an array nums of n integers where n > 1,  return an array output such that output[i] 
    is equal to the product of all the elements of nums except nums[i].

    Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array 
    (including the whole array) fits in a 32 bit integer.

    Note: Solve it without division and in O(n).
    """
    n = len(nums)
    L, R = [1] * n, [1] * n

    for i in range(1, n):
        L[i] = nums[i-1] * L[i-1]

    for i in range(n-2, -1, -1):
        R[i] = nums[i+1] * R[i+1]

    return [L[i] * R[i] for i in range(n)]


def prod_except_self_space_efficient(nums: List[int]) -> List[int]:
    """
    This solution uses O(1) space, not including output array!
    """
    n = len(nums)
    res = [1] * n

    for i in range(1, n):
        res[i] = nums[i-1] * res[i-1]

    R = 1
    for i in range(n-1, -1, -1):
        res[i] = R * res[i]
        R *= nums[i]

    return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    assert prod_except_self(nums) == [24, 12, 8, 6]
    assert prod_except_self_space_efficient(nums) == [24, 12, 8, 6]

    print("Passed all tests!")
