import heapq
from typing import List
from collections import Counter


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    # 347: Given a non-empty array of integers, return the k most frequent elements.
    """
    res, heap = [], []
    for num, cnt in Counter(nums).items():
        heap.append((-cnt, num))

    i = 0
    heapq.heapify(heap)
    while i < k:
        res.append(heapq.heappop(heap)[1])
        i += 1

    return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    assert top_k_frequent(nums, 2) == [1, 2]

    nums = [1]
    assert top_k_frequent(nums, 1) == [1]

    print("Passed all tests!")
