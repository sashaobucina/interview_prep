from typing import List
from itertools import product
from collections import defaultdict


def four_sum(nums: List[int], target: int) -> List[int]:
    """
    # 18: Given an array nums of n integers and an integer target, are there elements a, b, c, and d 
    in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives 
    the sum of target.

    NOTE: The solution set must not contain duplicate quadruplets.
    """
    ans = []

    for i in range(len(nums)):
        if i != 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums)):
            if j != i + 1 and nums[j] == nums[j - 1]:
                continue

            k, l = j + 1, len(nums) - 1

            while k < l:
                if nums[i] + nums[j] + nums[k] + nums[l] == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                    k += 1
                else:
                    l -= 1

    return ans


def four_sum_II(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    """
    # 454: Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) 
    there are such that A[i] + B[j] + C[k] + D[l] is zero.
    """
    ans = 0
    cache = defaultdict(int)

    for a, b in product(A, B):
        cache[a + b] += 1

    for c, d in product(C, D):
        ans += cache[-(c + d)]

    return ans


if __name__ == "__main__":
    arr = [1, 0, -1, 0, -2, 2]
    assert four_sum(arr, 0) == [[0, 0, -2, 2]]

    arr = [0, 0, 0, 0]
    assert four_sum(arr, 0) == [[0, 0, 0, 0]]

    A, B, C, D = [1, 2], [-2, -1], [-1, 2], [0, 2]
    assert four_sum_II(A, B, C, D) == 2

    A, B, C, D = [-1,-1], [-1,1], [-1,1], [1,-1]
    assert four_sum_II(A, B, C, D) == 6

    print("Passed all tests!")
