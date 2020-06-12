from random import choice, seed


class RandomizedSet:
    """
    # 380: Design a data structure that supports all following operations in average O(1) time.

    1) insert(val): Inserts an item val to the set if not already present.
    2) remove(val): Removes an item val from the set if present.
    3) getRandom: Returns a random element from current set of elements.
        Each element must have the same probability of being returned.
    """

    def __init__(self):
        self.hash = {}
        self.elements = []

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False

        size = len(self.elements)
        self.hash[val] = size
        self.elements.append(val)

        return True

    def remove(self, val) -> bool:
        idx = self.hash.get(val, None)
        if idx is None:
            return False

        del self.hash[val]

        # swap removed element w/ last element so removal is O(1) time
        last_val = self.elements[-1]
        if idx != len(self.elements) - 1:
            self.elements[idx], self.elements[-1] = self.elements[-1], self.elements[idx]
            self.hash[last_val] = idx

        self.elements.pop()

        return True

    def get_random(self) -> int:
        if len(self.elements) == 0:
            return -1

        return choice(self.elements)


if __name__ == "__main__":
    # set the random seed, for consistent testing
    seed(1)

    r_set = RandomizedSet()
    assert r_set.insert(1)
    assert not r_set.remove(2)
    assert r_set.insert(2)
    assert r_set.get_random() == 1
    assert r_set.remove(1)
    assert not r_set.insert(2)
    assert r_set.get_random() == 2

    print("Passed all tests!")
