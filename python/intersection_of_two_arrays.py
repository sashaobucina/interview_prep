from collections import Counter
from typing import List


def intersect(l1: List[int], l2: List[int]) -> List[int]:
    """
    # 349: Given two arrays, write a function to compute their intersection.

    NOTE:
    - Each element in the result must be unique.
    - The result can be in any order.
    """
    return list(set(l1).intersection(set(l2)))


def intersect_II(l1: List[int], l2: List[int]) -> List[int]:
    """
    # 350: Given two arrays, write a function to compute their intersection.
    
    NOTE:
    - Each element in the result should appear as many times as it shows in both arrays.
    - The result can be in any order.
    """
    res = []
    d = dict(Counter(l1))

    for num in l2:
        if d.get(num, 0) > 0:
            res.append(num)
            d[num] -= 1

    return res


if __name__ == "__main__":
    l1, l2 = [1, 2, 2, 1], [2, 2]
    assert intersect(l1, l2) == [2]

    assert intersect_II(l1, l2) == [2, 2]

    print("Passed all tests!")
