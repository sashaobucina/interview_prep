from typing import List


def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    # 47: Given a collection of numbers that might contain duplicates, return all possible unique permutations.
    """
    nums.sort()

    res = []
    N = len(nums)
    visited = set()

    def helper(arr):
        if len(arr) == N:
            res.append(arr)
            return

        for i, num in enumerate(nums):
            if (i in visited) or (i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited):
                continue

            visited.add(i)
            helper(arr + [num])
            visited.remove(i)

    helper([])
    return res


if __name__ == "__main__":
    nums = [1, 1, 2]
    assert permute_unique(nums) == [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ]

    print("Passed all tests!")
