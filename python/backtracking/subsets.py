from typing import List


def subsets(nums: list) -> list:
    """
    # 78: Given a set of distinct integers, return all possible subsets (the power set).

    NOTE: Do not return any duplicate subsets
    """
    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            currSubset = subsets[i]
            subsets.append(currSubset + [num])

    return subsets


def subsets_alt(nums: List[int]) -> List[List[int]]:
    subsets = [[]]

    def _helper(nums, acc):
        subsets.append(acc)

        for i, num in enumerate(nums):
            _helper(nums[i+1:], acc + [num])

    for i in range(len(nums)):
        _helper(nums[i+1:], [nums[i]])

    return subsets


def subsets_II(nums: List[int]) -> List[List[int]]:
    """
    # 90: Given a list of integers that may contain duplicates, return all possible subsets (the power set).

    NOTE: Do not return any duplicate subsets
    """
    if not nums or len(nums) == 0:
        return []

    nums = sorted(nums)
    result = []
    subset = []
    toFindAllSubsets(nums, result, subset, 0)
    return result


def toFindAllSubsets(nums: list, result: list, subset: list, start: int) -> None:
    result.append(subset.copy())
    for i in range(start, len(nums)):
        if (i != start and nums[i] == nums[i - 1]):
            continue
        subset.append(nums[i])
        toFindAllSubsets(nums, result, subset, i + 1)
        subset.pop()


if __name__ == "__main__":
    nums = [1, 2, 3]
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert subsets(nums) == expected

    nums = [1, 2, 2]
    expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert subsets_II(nums) == expected

    print("Passed all tests!")
