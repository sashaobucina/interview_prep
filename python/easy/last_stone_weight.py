from typing import List
import heapq


def last_stone_weight(stones: List[int]) -> int:
    """
    # 1046: We have a collection of stones, each stone has a positive integer weight.
    Each turn, we choose the two heaviest stones and smash them together. 

    Suppose the stones have weights x and y with x <= y.  The result of this smash is:
    - If x == y, both stones are totally destroyed;
    - If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

    At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
    """
    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        last = heapq.heappop(stones)
        sec_last = heapq.heappop(stones)

        if last != sec_last:
            heapq.heappush(stones, last - sec_last)

    return -stones[0] if stones else 0


if __name__ == "__main__":
    stones = [2, 7, 4, 1, 8, 1]
    assert last_stone_weight(stones) == 1

    stones = [5, 70, 74, 100, 106]
    assert last_stone_weight(stones) == 3

    print("Passed all tests!")
