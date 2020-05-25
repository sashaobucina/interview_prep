from typing import List
from collections import defaultdict


def min_set_size(nums: List[int]) -> int:
    """
    # 1338: Given an array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.
    Return the minimum size of the set so that at least half of the integers of the array are removed.

    Conditions:
    - 1 <= arr.length <= 10^5
    - arr.length is even.
    - 1 <= arr[i] <= 10^5
    """
    if len(nums) % 2 != 0:
        raise ValueError("arr must have an even length!")

    d = defaultdict(int)
    removed, target = 0, len(nums) // 2

    for num in nums:
        d[num] += 1

    sorted_counts = sorted(d.values(), reverse=True)

    for i, val in enumerate(sorted_counts):
        removed += val
        if removed >= target:
            return i + 1

    raise RuntimeError("Should not be here!")


if __name__ == "__main__":
    nums = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
    print(min_set_size(nums))    # Expected: 2

    nums = [7,7,7,7,7,7]
    print(min_set_size(nums))   # Expected: 1

    nums = [1,2,3,4,5,6,7,8,9,10]
    print(min_set_size(nums))   # Expected: 5
