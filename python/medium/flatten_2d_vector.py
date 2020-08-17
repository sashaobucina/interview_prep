from typing import List


class Vector2D:
    """
    # 251: Design and implement an iterator to flatten a 2d vector. It should support the following 
    operations: next and hasNext.
    """

    def __init__(self, v: List[List[int]]):
        self.vector = v
        self.inner = 0
        self.outer = 0

    def _advance_to_next(self):
        while self.outer < len(self.vector) and self.inner == len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0

    def next(self) -> int:
        self._advance_to_next()
        val = self.vector[self.outer][self.inner]
        self.inner += 1

        return val

    def hasNext(self) -> bool:
        self._advance_to_next()
        return self.outer < len(self.vector)


if __name__ == "__main__":
    vector_2d = Vector2D([[1, 2], [3], [4]])
    assert vector_2d.next() == 1
    assert vector_2d.next() == 2
    assert vector_2d.hasNext()
    assert vector_2d.next() == 3
    assert vector_2d.hasNext()
    assert vector_2d.next() == 4
    assert not vector_2d.hasNext()

    print("Passed all tests!")
