from typing import List
from collections import defaultdict


def subarray_sum(nums: List[int], k: int) -> int:
    """
    # 560: Given an array of integers and an integer k, you need to find the total number of continuous
    subarrays whose sum equals to k.
    """
    count = _sum = 0
    d = defaultdict(int)
    d[0] = 1

    for num in nums:
        _sum += num
        diff = _sum - k

        if diff in d:
            count += d[diff]

        d[_sum] += 1

    return count


if __name__ == "__main__":
    nums = [1, 1, 1]
    assert subarray_sum(nums, 2) == 2

    print("Passed all tests!")
