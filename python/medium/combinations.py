from typing import List


def combinations(n: int, k: int) -> List[List[int]]:
    """
    # 77: Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
    """
    ans = []

    def _backtrack(idx: int, path: List[int]):
        if len(path) == k:
            ans.append(path)
            return

        for i in range(idx, n + 1):
            _backtrack(i + 1, path + [i])

    _backtrack(1, [])
    return ans


if __name__ == "__main__":
    assert combinations(n=4, k=2) == [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4]
    ]

    print("Passed all tests!")
