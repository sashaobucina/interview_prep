from typing import List


def combination_sum(candidates: list, target: int) -> list:
    """
    Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
    find all unique combinations in candidates where the candidate numbers sums to target.

    The same repeated number may be chosen from candidates unlimited number of times.

    NOTE: Time complexity is O(n!)
    """
    def backtrack(subset=[], sum=0, n=0):
        if sum == target:
            ans.append(subset)
            return
        for i in range(n, len(candidates)):
            num = candidates[i]
            if sum + num <= target:
                backtrack(subset + [num], sum + num, i)
    ans = []
    if candidates:
        for i, num in enumerate(candidates):
            backtrack([num], num, i)
    return ans


def combination_sum_II(candidates: list, target: int) -> list:
    """
    Given a collection of candidate numbers (candidates) and a target number (target), find all 
    unique combinations in candidates where the candidate numbers sums to target.

    Each number in candidates may only be used once in the combination.

    NOTE:
    - All numbers (including target) will be positive integers.
    - The solution set must not contain duplicate combinations.
    """
    candidates.sort()
    sums, n = [], len(candidates)

    def find_combos(subset: list, sum: int, start: int) -> None:
        if sum == target:
            sums.append(subset)
            return

        for i in range(start, n):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            num = candidates[i]
            if sum + num <= target:
                find_combos(subset + [num], sum + num, i + 1)

    find_combos([], 0, 0)
    return sums


def combination_sum_IV(nums: List[int], target: int) -> int:
    """
    # 377: Given an integer array with all positive numbers and no duplicates, find the number of possible 
    combinations that add up to a positive integer target.

    Backtracking time complexity - O(n!)
    DP time complexity - O(target * n)
    """
    count = [0]

    def _backtrack(curr, target):
        if curr == target:
            count[0] += 1
            return
        if curr > target:
            return
        for i in range(len(nums)):
            curr += nums[i]
            _backtrack(curr, target)
            curr -= nums[i]

    def _dp():
        memo = [0] * (target + 1)
        for i in range(len(memo)):
            for j in nums:
                if i == j:
                    memo[i] += 1
                elif (i - j) > 0:
                    memo[i] += memo[i-j]

        return memo[-1]

    return _dp()


if __name__ == "__main__":
    arr = [6, 3, 7, 2]
    assert combination_sum(arr, 8) == [[6, 2], [3, 3, 2], [2, 2, 2, 2]]

    arr2 = [10, 1, 2, 7, 6, 1, 5]
    assert combination_sum_II(arr2, 8) == [[1, 1, 6], [
        1, 2, 5], [1, 7], [2, 6]]

    arr3 = [1, 2, 3, 4]
    assert combination_sum_IV(arr3, 4) == 8

    print("Passed all tests!")
