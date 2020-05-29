import random
from typing import List


class ShuffledList:
    """
    # 384: Shuffle a set of numbers without duplicates.
    """

    def __init__(self, nums: List[int]):
        self.orig = nums
        self.nums = list(nums)

    def reset(self) -> List[int]:
        self.nums = list(self.orig)
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            rand_idx = random.randrange(i, n)
            self.nums[i], self.nums[rand_idx] = self.nums[rand_idx], self.nums[i]
        return self.nums


if __name__ == "__main__":
    nums = [1, 2, 3]
    obj = ShuffledList(nums)
    obj.shuffle()
    obj.shuffle()
    assert nums == obj.reset()

    print("Passed all tests!")
