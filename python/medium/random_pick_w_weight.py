import random
from typing import List


random.seed(0)


def rand_pick_with_weights(weights):
    """
    # 528: Given an array w of positive integers, where w[i] describes the weight of index i, 
    write a function pickIndex which randomly picks an index in proportion to its weight.

    NOTE:
    - 1 <= w.length <= 10000
    - 1 <= w[i] <= 10^5
    - pickIndex will be called at most 10000 times
    """

    # get prefix sum of weights
    presum = _prefix_sum(weights)
    target = random.randrange(0, presum[-1]) + 1

    # binary search for target in prefix sum of weights
    left, right = 0, len(presum) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if target > presum[mid]:
            left = mid + 1
        else:
            right = mid

    return left if presum[left] >= target else right


def _prefix_sum(lst: List[int]) -> List[int]:
    """ Naive prefix sum algorithm. """
    if not lst:
        return []

    res = [0] * len(lst)
    res[0] = lst[0]

    for i in range(1, len(lst)):
        res[i] = res[i - 1] + lst[i]

    return res


if __name__ == "__main__":
    assert rand_pick_with_weights([1, 3, 1]) == 1

    print("Passed all tests!")
