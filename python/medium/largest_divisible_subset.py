from typing import List


def largest_divisible_subset(nums: List[int]) -> List[int]:
    """
    # 368: Given a set of distinct positive integers, find the largest subset such that every pair 
    (Si, Sj) of elements in this subset satisfies:

    - Si % Sj = 0 or Sj % Si = 0. If there are multiple solutions, return any subset is fine.

    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    if not nums:
        return []

    # sort to ensure divisors of element show up before
    nums.sort()

    max_idx = 0
    div_count = [1 for _ in range(len(nums))]
    prev = [None for _ in range(len(nums))]

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if div_count[i] <= div_count[j]:
                    div_count[i] = div_count[j] + 1
                    prev[i] = j

        # update max index so far
        if div_count[max_idx] < div_count[i]:
            max_idx = i

    # construct largest subset, from max index down using prev list chain
    largest_subset = []
    while max_idx is not None:
        largest_subset.append(nums[max_idx])
        max_idx = prev[max_idx]

    return largest_subset[::-1]


if __name__ == "__main__":
    arr = []
    assert largest_divisible_subset(arr) == []

    arr = [100]
    assert largest_divisible_subset(arr) == arr

    arr = [1, 2, 3]
    assert largest_divisible_subset(arr) == [1, 2]

    arr = [1, 2, 4, 8]
    assert largest_divisible_subset(arr) == arr

    arr = [2, 4, 3, 8]
    assert largest_divisible_subset(arr) == [2, 4, 8]

    print("Passed all tests!")
