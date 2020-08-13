from collections import deque


class CombinationIterator:
    """
    # 1286: Design an Iterator class, which has:
        - A constructor that takes a string characters of sorted distinct lowercase English letters and 
            a number combinationLength as arguments.
        - A function next() that returns the next combination of length combinationLength in lexicographical order.
        - A function hasNext() that returns True if and only if there exists a next combination.

    NOTE: This solution precomputes all answers
    """

    def __init__(self, characters: str, combinationLength: int):
        self.combos = deque(self._combinations(characters, combinationLength))

    def next(self) -> str:
        return self.combos.popleft()

    def hasNext(self) -> bool:
        return len(self.combos) > 0

    def _combinations(self, chs, combo_len):
        N = len(chs)
        ans = []

        def _backtrack(s, idx):
            if len(s) == combo_len:
                ans.append("".join(s))
                return

            for i in range(idx, N):
                _backtrack(s + [chs[i]], i + 1)

        _backtrack([], 0)
        return ans


if __name__ == "__main__":
    iterator = CombinationIterator("abc", 2)
    assert iterator.next() == "ab"
    assert iterator.hasNext()
    assert iterator.next() == "ac"
    assert iterator.hasNext()
    assert iterator.next() == "bc"
    assert not iterator.hasNext()

    print("Passed all tests!")
